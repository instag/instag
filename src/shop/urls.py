from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^me$', views.ShowShop.as_view(), name='show_self'),
    url(r'^shop/edit$', views.EditShop.as_view(), name='edit'),
    url(r'^(?P<slug>[\w\-]+)$', views.ShowShop.as_view(), name='show'),
]
1