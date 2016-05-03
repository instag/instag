# -*- coding: utf-8 -*-
from common import template_text as T
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.views import generic
from instagram import client
from instagram_url.models import InstagramPlayer, InstagramPlayerMedia
from shop.models import Shop
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

CONFIG = T.CONFIG
unauthenticated_api = client.InstagramAPI(**CONFIG)

class HomePage(generic.TemplateView):
    template_name = "home.html"
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        url = unauthenticated_api.get_authorize_url(scope=["likes","comments"])
        user = self.request.user
        instagram_player = InstagramPlayer.get_instagram_play(user_site_id=user.id)


        paginator = Paginator(InstagramPlayerMedia.get_all(), self.paginate_by)
        page = self.request.GET.get('page')

        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        kwargs["media"] = page_obj
        kwargs["page_obj"] = page_obj
        kwargs["instagram_player"] = instagram_player
        kwargs["url_test"] = url

        #ログインユーザ
        if instagram_player:
            shop = Shop.objects.get_or_create(user=instagram_player)
            kwargs["shop"] = shop[0]
            kwargs["profile_picture"] = instagram_player.profile_picture

        return super(HomePage, self).get(request, *args, **kwargs)

class SearchPage(generic.TemplateView):
    template_name = "search.html"
    paginate_by = 10

    def get(self, request, *args, **kwargs):

        search_tag = request.GET.get('search_tag')
        tag_search, next_tag = unauthenticated_api.tag_search(search_tag.encode('utf8'))
        tag_recent_media, next = unauthenticated_api.tag_recent_media(tag_name=tag_search[0].name)
        kwargs['tag_recent_media'] = tag_recent_media
        kwargs['search_tag'] = search_tag
        return super(SearchPage, self).get(request, *args, **kwargs)

class AboutPage(generic.TemplateView):
    template_name = "about.html"

class ShopListPage(generic.TemplateView):
    template_name = "shop_list.html"
