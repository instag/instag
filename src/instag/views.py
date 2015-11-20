from django.views import generic
from instagram import client, subscriptions


session_opts = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True,
}

CONFIG = {
    'client_id': '3dc77d748ec9434fba8d92569824b5ea',
    'client_secret': '44dafb59c4d94095a0a326022d7e82c1',
    'redirect_uri': 'http://localhost:8515/oauth_callback'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)



class HomePage(generic.TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, *args, **kwargs):
        print 2222
        url = unauthenticated_api.get_authorize_url(scope=["likes","comments"])
        url_test = '<a href="%s">Connect with Instagram</a>' % url
        
        return {"url_test": url, "blocked_media": "test"}
    


class AboutPage(generic.TemplateView):
    template_name = "about.html"
