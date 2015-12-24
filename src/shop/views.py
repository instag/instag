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
    # template_name = "shop/shop_show.html"
    # http_method_names = ['get']
    template_name = "shop/shop_show.html"

    # def get(self, request, *args, **kwargs):
    def get_context_data(self, *args, **kwargs):
        print 11
        print self
        print self.request
        print self.request.user

        user = self.request.user
        print 22
        instagram_player = InstagramPlayer.objects.get(user_site_id=user.id)
        print 33
        shop = Shop.objects.get(user=instagram_player)
        print 4544
        insta_user_media = InstagramPlayerMedia.get_player_media_list(instagram_player)

        print 55
        kwargs["shop"] = shop
        kwargs["profile_picture"] = instagram_player.profile_picture
        kwargs["media"] = insta_user_media

        return {"profile_picture": instagram_player.profile_picture,
                "media":insta_user_media,
                "shop":shop
                }


        # return super(ShowShop, self).dispatch(self.request, *args, **kwargs)


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
        print request.POST['shop_title']
        print request.POST['shop_description']

        shop_title = request.POST['shop_title']
        shop_description = request.POST['shop_description']

        result = Shop.get_or_create(user.id)
        result.shop_title = shop_title
        result.shop_description = shop_description
        result.save()

        messages.success(request, " details saved!")
        return redirect("shop:show_self")