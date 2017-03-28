from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$', views.Felica.as_view(), name='felica_self'),
]
