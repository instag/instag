# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.views import generic
from instagram_url.models import InstagramPlayer, InstagramPlayerMedia

from . import forms
from .models import Shop


class ShowShop(LoginRequiredMixin, generic.TemplateView):
    template_name = "shop/shop_show.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        instagram_player = InstagramPlayer.objects.get_instagram_play(user_site_id=user.id)
        shop = Shop.objects.get_or_create(user=instagram_player)
        insta_user_media = InstagramPlayerMedia.get_player_media_list(instagram_player)

        kwargs["shop"] = shop[0]
        if instagram_player:
            kwargs["profile_picture"] = instagram_player.profile_picture
        kwargs["media"] = insta_user_media

        return super(ShowShop, self).get(request, *args, **kwargs)


class EditShop(LoginRequiredMixin, generic.TemplateView):
    
    template_name = "shop/shop_edit.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        instagram_player = InstagramPlayer.objects.get(user_site_id=user.id)
        shop = Shop.objects.get(user=instagram_player)

        if "shop_form" not in kwargs:
            kwargs["shop_form"] = forms.ShopForm(instance=shop)

        kwargs["profile_picture"] = instagram_player.profile_picture
        return super(EditShop, self).get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        user = self.request.user

        shop_title = request.POST['shop_title']
        shop_description = request.POST['shop_description']

        result = Shop.get_or_create(user.id)
        result.shop_title = shop_title
        result.shop_description = shop_description
        result.save()

        messages.success(request, " details saved!")
        return redirect("shop:show_self")