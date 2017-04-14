from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$', views.Felica.as_view(), name='felica_self'),
        url(r'^felica/member/list$', views.FelicaMemberList.as_view(), name='felica_member_list'),
        url(r'^felica/work/time$', views.FelicaWorkTime.as_view(), name='felica_work_time'),
        url(r'^felica/member/edit/(?P<id>[\w\-]+)$', views.FelicaMemberEdit.as_view(), name='felica_member_edit'),
]
