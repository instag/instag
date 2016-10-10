# -*- coding: utf-8 -*-
import sys
import urllib2

from common import template_text as T
from django.http import HttpResponse
from django.views import generic
from instagram import client
from django.http import HttpResponse
from instagram_url.models import InstagramPlayer, InstagramPlayerMedia
from snscom import utils as snscom_utils
from apiclient.discovery import build
# from django.core.cache import cache
from django.core.cache import caches
from django.core.cache import cache
import time, datetime


reload(sys)
sys.setdefaultencoding("utf-8")
import json

CONFIG = T.CONFIG
unauthenticated_api = client.InstagramAPI(**CONFIG)


CACHE_KR = 3600 * 24
CACHE_JP = 3600 * 24
CACHE_POP = 3600 * 24
CACHE_SK_LIST = 3600 * 24
CACHE_POP_LIST = 3600 * 24
TOP_100_KR_COUNT = 100
TOP_100_JP_COUNT = 100
IS_NEW_SONG_DAYS_JPOP = 10
CACHE_KEY_SONG = 'song_title_list'
CACHE_KEY = 'KPOP100'

DEVELOPER_KEY = "AIzaSyAcwCMEw4IWmUalZSEG1SGXpMnMAcdcLKA"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class Snscom(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        print "get_snscom"
        response = HttpResponse(json.dumps({'test':'test_value'}), content_type="application/json", status=200)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'

        return response.GET
        return response.POST

    def post(self, request, *args, **kwargs):
        print "post_snscom"
        return HttpResponse("ok")

class Profile(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        list = [{
        "title": "라면?",
        "detail": "A shirt with plain design.",
        "img": "http://ecx.images-amazon.com/images/I/51edhsNSz8L._AC_US160_.jpg"},
      {"title": "골프모임",
        "detail": "A shirt with plain design.",
        "img": "http://ecx.images-amazon.com/images/I/41JREil%2B3sL.jpg"}]

        response = HttpResponse(json.dumps({'test':list}), content_type="application/json", status=200)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'

        return response

    def post(self, request, *args, **kwargs):
        print "post_profile"
        return HttpResponse("ok")


class SKSearch(generic.TemplateView):

    def get(self, request, *args, **kwargs):

        song_list = snscom_utils.get_kpop_list()

        return song_list

class KpopRank(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        import logging
        # logging.error("kpopRank")

        out = caches['default'].get(T.CACHE_KEY_KPOP_LIST)
        if out is None:
            out = snscom_utils.get_youtube_list(snscom_utils.get_kpop_list(), 'KR', T.CACHE_KEY_KPOP_LIST, 'KR')

        return snscom_utils.get_response(out)

class JpopRank(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        # out = cache.get(T.CACHE_KEY_JPOP_LIST, None)
        out = caches['default'].get(T.CACHE_KEY_JPOP_LIST)
        if out is None:
            out = snscom_utils.get_youtube_list(snscom_utils.get_jpop_list(), 'JP', T.CACHE_KEY_JPOP_LIST, 'JP')
        return snscom_utils.get_response(out)

class PopRank(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        out = cache.get(T.CACHE_KEY_POP_LIST, None)
        if out is None:
            out = snscom_utils.get_youtube_list(snscom_utils.get_pop_list(), 'JP', T.CACHE_KEY_POP_LIST, 'USA')
        return snscom_utils.get_response(out)
