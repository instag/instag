from django.conf.urls import url
from . import views


print 11
urlpatterns = [
    # url(r'^$', views.Snscom.as_view(), name='snscom_self'),
    url(r'^tags/$', views.Snscom.as_view(), name='tags_self'),
    url(r'^test/test/$', views.Snscom.as_view(), name='tags_self'),
]
