from common import template_text as T
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.views import generic
from instagram import client
from instagram_url.models import InstagramPlayer, InstagramPlayerMedia
from shop.models import Shop

CONFIG = T.CONFIG

unauthenticated_api = client.InstagramAPI(**CONFIG)

class HomePage(generic.TemplateView):
    template_name = "home.html"
    paginate_by = 20


    def get(self, request, *args, **kwargs):
        # url = unauthenticated_api.get_authorize_url(scope=["likes","comments"])

        user = self.request.user
        # instagram_player = InstagramPlayer.objects.get(user_site_id=user.id)
        instagram_player = InstagramPlayer.get_instagram_play(user_site_id=user.id)
        if instagram_player:
            shop = Shop.objects.get_or_create(user=instagram_player)
            insta_user_media = InstagramPlayerMedia.get_player_media_list(instagram_player)
            paginator = Paginator(insta_user_media, self.paginate_by)
            page = self.request.GET.get('page')

            try:
                page_obj = paginator.page(page)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)

            kwargs["page_obj"] = page_obj
            kwargs["shop"] = shop[0]
            kwargs["profile_picture"] = instagram_player.profile_picture
            kwargs["media"] = page_obj
        else :
            kwargs["media"] = InstagramPlayerMedia.get_all()


        return super(HomePage, self).get(request, *args, **kwargs)


class AboutPage(generic.TemplateView):
    template_name = "about.html"
