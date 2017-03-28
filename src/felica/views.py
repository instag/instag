# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.views import generic
from instagram_url.models import InstagramPlayer, InstagramPlayerMedia

from . import forms
from .models import Shop

import sys
from common import template_text as T
from django.http import HttpResponse
from django.http import HttpResponse
from django.views import generic
from instagram import client
from snscom import utils as snscom_utils
from django.core.cache import caches
from instagram_url.models import InstagramPlayerMedia
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
reload(sys)
sys.setdefaultencoding("utf-8")
import json
import logging

CONFIG = T.CONFIG
unauthenticated_api = client.InstagramAPI(**CONFIG)





class Felica(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        print "felica.....1"

        print request
        print request.GET
        print args
        print kwargs

        # response = HttpResponse(json.dumps({'test':'test_value'}), content_type="application/json", status=200)
        # response['Access-Control-Allow-Origin'] = '*'
        # response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'

        # return response.GET
        # return response.POST

    def post(self, request, *args, **kwargs):
        print "felica...2"
        # return HttpResponse("ok")
#
# class ShowShop(LoginRequiredMixin, generic.TemplateView):
#     template_name = "shop/shop_show.html"
#     http_method_names = ['get']
#
#     def get(self, request, *args, **kwargs):
#         user = self.request.user
#         instagram_player = InstagramPlayer.get_instagram_play(user_site_id=user.id)
#         shop = Shop.objects.get_or_create(user=instagram_player)
#         insta_user_media = InstagramPlayerMedia.get_player_media_list(instagram_player)
#
#         kwargs["shop"] = shop[0]
#         if instagram_player:
#             kwargs["profile_picture"] = instagram_player.profile_picture
#         kwargs["media"] = insta_user_media
#
#         return super(ShowShop, self).get(request, *args, **kwargs)
#
#
# class EditShop(LoginRequiredMixin, generic.TemplateView):
#
#     template_name = "shop/shop_edit.html"
#     http_method_names = ['get', 'post']
#
#     def get(self, request, *args, **kwargs):
#         user = self.request.user
#         instagram_player = InstagramPlayer.objects.get(user_site_id=user.id)
#         shop = Shop.objects.get(user=instagram_player)
#
#         if "shop_form" not in kwargs:
#             kwargs["shop_form"] = forms.ShopForm(instance=shop)
#
#         kwargs["profile_picture"] = instagram_player.profile_picture
#         return super(EditShop, self).get(request, *args, **kwargs)
#
#
#     def post(self, request, *args, **kwargs):
#         user = self.request.user
#
#         shop_title = request.POST['shop_title']
#         shop_description = request.POST['shop_description']
#
#         result = Shop.get_or_create(user.id)
#         result.shop_title = shop_title
#         result.shop_description = shop_description
#         result.save()
#
#         messages.success(request, " details saved!")
#         return redirect("shop:show_self")