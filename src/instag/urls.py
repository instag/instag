from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import minsta.urls
import shop.urls
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),

    url(r'^search/$', views.SearchPage.as_view(), name='search'),

    url(r'^shop_list/$', views.ShopListPage.as_view(), name='shop_list'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^minsta/', include(minsta.urls, namespace='minsta')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^shop', include(shop.urls, namespace='shop')),

]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

