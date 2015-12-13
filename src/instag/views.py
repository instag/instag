from django.views import generic
from instagram import client, subscriptions
from .hostname import HOSTNAME

session_opts = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True,
}

print 222
CONFIG = {
    'client_id': '3dc77d748ec9434fba8d92569824b5ea',
    'client_secret': '44dafb59c4d94095a0a326022d7e82c1',
    'redirect_uri': 'http://127.0.0.1:8060/minsta/'
}

if HOSTNAME.startswith('wishtag.net'):
    CONFIG = {
        'client_id': '3dc77d748ec9434fba8d92569824b5ea',
        'client_secret': '44dafb59c4d94095a0a326022d7e82c1',
        'redirect_uri': 'http://ec2-52-68-85-32.ap-northeast-1.compute.amazonaws.com/minsta/'
    }

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
        
        print "======== START"
        print site_user.id
        print "======== END"
        
        
        
        return {"url_test": url, "blocked_media": "test"}
    

class AboutPage(generic.TemplateView):
    template_name = "about.html"
