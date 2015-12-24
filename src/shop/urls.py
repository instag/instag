from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^me$', views.ShowShop.as_view(), name='show_self'),
    url(r'^me/edit$', views.EditShop.as_view(), name='edit_self'),
    url(r'^(?P<slug>[\w\-]+)$', views.ShowShop.as_view(),
        name='show'),
]
