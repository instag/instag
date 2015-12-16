# -*- coding: UTF-8 -*-
from braces.views import JSONResponseMixin, AjaxResponseMixin
from django.core.cache import cache
from django.contrib.auth.decorators import user_passes_test
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, RedirectView, DeleteView, View
from instagram import InstagramAPIError
from instagram.client import InstagramAPI
from instagram_url import api as in_api
from instagram_url.models import InstagramPlayer
from mezzanine.conf import settings
from .models import Instagram, Media
from instagram import client, subscriptions

import logging
import hmac
from hashlib import sha256

CONFIG = {
    'client_id': '3dc77d748ec9434fba8d92569824b5ea',
    'client_secret': '44dafb59c4d94095a0a326022d7e82c1',
    'redirect_uri': 'http://127.0.0.1:8060/minsta/'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)

logger = logging.getLogger(__name__)
client_id = settings.INSTAGRAM_CLIENT_ID
client_secret = settings.INSTAGRAM_CLIENT_SECRET
redirect_uri = "http://127.0.0.1:8060/minsta/"
api_insta = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

class InstagramView(TemplateView):
    template_name = "instagram/instagram_oauth.html"
    def get_context_data(self, *args, **kwargs):
        
        
        site_user = self.request.user
        code = self.request.GET.get('code')
        url = None
        access_token = None
        in_player = None
        insta_user = None
        
        # instagram apiからcode取得したら
        if code:
            
            if 'access_token' in self.request.session:
                # DB에서 취득
                access_token = self.request.session['access_token']
                instagram_player = InstagramPlayer.get_instagram_play(site_user.id)
                return {"profile_picture": instagram_player.profile_picture}
            
            else:
                # DB에서 취득
                access_token, user_info = unauthenticated_api.exchange_code_for_access_token(code)
                self.request.session['access_token'] = access_token
                if user_info:
                    instagram_player = in_api.get_instagram_player(user_info,
                                                            code,
                                                            access_token, 
                                                            site_user)
                    
                return {"profile_picture": instagram_player.profile_picture}

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
