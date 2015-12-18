# -*- coding: UTF-8 -*-
import logging

from braces.views import JSONResponseMixin, AjaxResponseMixin
from common import template_text as T
from django.contrib.auth.decorators import user_passes_test
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, RedirectView, DeleteView, View
from instagram import client
from instagram.client import InstagramAPI
from instagram_url import api as in_api
from mezzanine.conf import settings
import beaker.middleware
import bottle
from instagram_url.models import InstagramPlayer
from .models import Instagram, Media

CONFIG = T.CONFIG
unauthenticated_api = client.InstagramAPI(**CONFIG)

logger = logging.getLogger(__name__)
client_id = settings.INSTAGRAM_CLIENT_ID
client_secret = settings.INSTAGRAM_CLIENT_SECRET
app = beaker.middleware.SessionMiddleware(bottle.app(), T.session_opts)


class InstagramView(TemplateView):
    template_name = "instagram/instagram_oauth.html"

    def get_context_data(self, *args, **kwargs):
        site_user = self.request.user
        code = self.request.GET.get('code')
        url = None
        access_token = None
        in_player = None
        insta_user = None

        if site_user and code:
            access_token, user_info = unauthenticated_api.exchange_code_for_access_token(code)
            if user_info:
                instagram_player = in_api.get_instagram_player(user_info,
                                                               code,
                                                               access_token,
                                                               site_user)
                insta_user = InstagramPlayer.get_instagram_play(site_user.id)
                api = client.InstagramAPI(access_token=insta_user.oauth_token, client_secret=CONFIG['client_secret'])
                recent_media, next = api.user_recent_media()

            return {"profile_picture": instagram_player.profile_picture,
                    "media":recent_media}

        # MY샵의 경우
        if site_user:
            insta_user = InstagramPlayer.get_instagram_play(site_user.id)

            """
            api부분 삭제하고 db에서 취득하게 고쳐야 함
            """
            api = client.InstagramAPI(access_token=insta_user.oauth_token, client_secret=CONFIG['client_secret'])
            recent_media, next = api.user_recent_media()
        return {"profile_picture": insta_user.profile_picture,"media":recent_media}



class InstagramTagsView(TemplateView):
    template_name = "instagram/instagram.html"
    def get_context_data(self, *args, **kwargs):
        blocked = Media.objects.filter(allowed=False).values_list('media_id', flat=True)
        media = [m for m in cache.get('INSTAGRAM_TAGS_STREAM', []) if m.id not in blocked]
        return {"media": media, "blocked_media": blocked}


class InstagramOAuthView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        code = self.request.GET.get("code")
        settings.use_editable()
        site = Site.objects.get_current()
        
        conf = {
            "redirect_uri": "http://{0}{1}".format(site.domain, reverse('instagram_oauth')),
            "client_id": settings.INSTAGRAM_CLIENT_ID,
            "client_secret": settings.INSTAGRAM_CLIENT_SECRET,
        }
        unauthorized_api = InstagramAPI(**conf)
        logger.debug(unauthorized_api)
        access_token = unauthorized_api.exchange_code_for_access_token(code)
        try:
            instagram = Instagram.objects.all()[0]
            instagram.access_token = access_token[0]
            instagram.user_id = int(access_token[1]['id'])
            instagram.full_name = access_token[1]['full_name']
            instagram.username = access_token[1]['username']
            instagram.save()
        except IndexError:
            Instagram.objects.create(access_token=access_token[0],
                                     user_id=int(access_token[1]['id']),
                                     full_name=access_token[1]['full_name'],
                                     username=access_token[1]['username'])
        return "/admin/"


class InstagramDeleteView(DeleteView):
    success_url = "/admin/"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(InstagramDeleteView, self).dispatch(*args, **kwargs)

    def get_object(self):
        try:
            return Instagram.objects.all()[0]
        except IndexError:
            return None


class InstagramAjaxView(JSONResponseMixin, AjaxResponseMixin, View):
    """Instagram photos"""
    def get_ajax(self, request, *args, **kwargs):
        try:
            instagram = Instagram.objects.all()[0]
            api = InstagramAPI(access_token=instagram.access_token)
            media, discard = api.user_recent_media(
                user_id=instagram.user_id, count=24)
            json_dict = {
                "thumbnails": [{"url": n.images.get("thumbnail").url,
                           "width": n.images.get("thumbnail").width,
                           "height": n.images.get("thumbnail").height,
                           } for n in media],
                "low_resolution": [{"url": n.images.get("low_resolution").url,
                           "width": n.images.get("low_resolution").width,
                           "height": n.images.get("low_resolution").height,
                           } for n in media],
                "standard_resolution": [{"url": n.images.get("standard_resolution").url,
                           "width": n.images.get("standard_resolution").width,
                           "height": n.images.get("standard_resolution").height,
                           } for n in media],
                }
        except IndexError:
            json_dict = {
                "media": []
            }
        return self.render_json_response(json_dict)
