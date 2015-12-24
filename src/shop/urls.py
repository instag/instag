from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shop_show$', views.ShowShop.as_view(), name='shop_show'),
    url(r'^me/edit$', views.EditShop.as_view(), name='edit_self'),
    url(r'^(?P<slug>[\w\-]+)$', views.ShowShop.as_view(),
        name='show'),
]
