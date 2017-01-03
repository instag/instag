# from django.conf.urls import patterns, url

from .views import (
    InstagramView, InstagramTagsView,
    InstagramOAuthView, InstagramDeleteView, InstagramAjaxView
)

urlpatterns = [
    # url(r"^$", InstagramView.as_view(), name="instagram"),
    # url(r"^instag_main$", InstagramView.as_view(), name="instagram"),
    # url(r"^tags/$", InstagramTagsView.as_view(), name="instagram_tags"),
    # # url(r"^oauth/$", InstagramOAuthView.as_view(), name="instagram_oauth"),
    # url(r"^delete/$", InstagramDeleteView.as_view(), name="instagram_delete"),
    # url(r"^ajax/$", InstagramAjaxView.as_view(), name="instagram_ajax"),
]

