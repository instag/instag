from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^realtime_jp/$', views.RealtimeJP.as_view(), name='realtime_jp')

]
