from django.views import generic
from instagram import client, subscriptions
from .hostname import HOSTNAME
from common import template_text as T

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
    def get_context_data(self, *args, **kwargs):
        url = unauthenticated_api.get_authorize_url(scope=["likes","comments"])
        url_test = '<a href="%s">Connect with Instagram</a>' % url
        site_user = self.request.user
        return {"url_test": url, "blocked_media": "test"}
    

class AboutPage(generic.TemplateView):
    template_name = "about.html"
