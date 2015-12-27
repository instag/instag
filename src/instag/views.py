from django.views import generic
from instagram import client, subscriptions
from .hostname import HOSTNAME
from common import template_text as T
from instagram_url.models import InstagramPlayer, InstagramPlayerMedia
from shop.models import Shop


CONFIG = T.CONFIG

unauthenticated_api = client.InstagramAPI(**CONFIG)

#     def get(self, request, *args, **kwargs):
#         user = self.request.user
#         if "user_form" not in kwargs:
#             kwargs["user_form"] = forms.UserForm(instance=user)
#         if "profile_form" not in kwargs:
#             kwargs["profile_form"] = forms.ProfileForm(instance=user.profile)
#         return super(EditProfile, self).get(request, *args, **kwargs)
# 
#     def post(self, request, *args, **kwargs):



class HomePage(generic.TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        # url = unauthenticated_api.get_authorize_url(scope=["likes","comments"])

        user = self.request.user
        instagram_player = InstagramPlayer.objects.get(user_site_id=user.id)
        shop = Shop.objects.get_or_create(user=instagram_player)
        insta_user_media = InstagramPlayerMedia.get_player_media_list(instagram_player)
        kwargs["shop"] = shop[0]
        kwargs["profile_picture"] = instagram_player.profile_picture
        kwargs["media"] = insta_user_media

        return super(HomePage, self).get(request, *args, **kwargs)


class AboutPage(generic.TemplateView):
    template_name = "about.html"
