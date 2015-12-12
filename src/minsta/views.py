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
from mezzanine.conf import settings
from .models import Instagram, Media
from instagram import client, subscriptions

import logging
import hmac
from hashlib import sha256

def generate_sig(endpoint, params, secret):
    sig = endpoint
    for key in sorted(params.keys()):
        sig += '|%s=%s' % (key, params[key])
    return hmac.new(secret, sig, sha256).hexdigest()

logger = logging.getLogger(__name__)
client_id = settings.INSTAGRAM_CLIENT_ID
client_secret = settings.INSTAGRAM_CLIENT_SECRET
redirect_uri = "http://127.0.0.1:8060/minsta/"
api_insta = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

class InstagramView(TemplateView):
    template_name = "instagram/instagram.html"
    def get_context_data(self, *args, **kwargs):
        
        site_user = self.request.user
        code = self.request.GET.get('code')
        url = None
        access_token = None
        in_player = None
        insta_user = None

        if code:
            try:
                url = api_insta.get_authorize_url(scope=["relationships"])
                access_token, insta_user = api_insta.exchange_code_for_access_token(code)
                self.request.session['access_token'] = access_token
                if insta_user:
                    in_player = in_api.get_instagram_player(insta_user,
                                                            code,
                                                            access_token, 
                                                            site_user)
            except:
                pass
        
        else:
            access_token = self.request.session.get('access_token',None)
            in_player = in_api.get_instagram_player_token(access_token)
        
        
        
        
        endpoint = '/media/657988443280050001_25025320'
        params = {
            'access_token': access_token,
            'count': 10,
        }
        secret = client_secret
        sig = generate_sig(endpoint, params, secret)
        
        
        
        try:
            instagram = Instagram.get_or_create_user(access_token, 
                                                     in_player.user_name, 
                                                     in_player.user_id)
            
#             api = InstagramAPI(client_secret=client_secret,access_token=instagram.access_token)
            
            print 1111
            api = client.InstagramAPI(access_token=access_token, client_secret=client_secret)
            print access_token
            print client_secret
            print 222
            

            print 3333
            print api
            media, next = api.user_recent_media()
            print 44444
            print media

            
            try:
                    print 999
#                     print api
#                     media, next = api.user_recent_media()
#                     print 44444
#                     print media
#                 media, discard = api.user_recent_media(user_id=instagram.user_id,count=10)

            except InstagramAPIError as e:
                print e
                logger.error(e)
                return {"media": []}
            return {"media": media}
        except IndexError:
            return {"media": []}


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
