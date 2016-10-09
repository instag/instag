from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Snscom.as_view(), name='snscom_self'),
    url(r'^profile/$', views.Profile.as_view(), name='profile_self'),
    url(r'^tags/$', views.Snscom.as_view(), name='tags_self'),
    url(r'^test/test/$', views.Snscom.as_view(), name='tags_self'),
    url(r'^sksearch/$', views.SKSearch.as_view(), name='sksearch_self'),
    url(r'^kpoprank/$', views.KpopRank.as_view(), name='kpop_rank'),
    url(r'^jpoprank/$', views.JpopRank.as_view(), name='jpop_rank'),
    url(r'^poprank/$', views.PopRank.as_view(), name='pop_rank')
]
