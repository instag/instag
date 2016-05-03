# -*- coding: utf-8 -*-
from common import template_text as T
from django.core.management.base import BaseCommand
from instagram import client
from instagram_url.models import InstagramPlayer, InstagramPlayerMedia
import urllib2
import urllib
import cgi
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

CONFIG = T.CONFIG
unauthenticated_api = client.InstagramAPI(**CONFIG)

class Command(BaseCommand):
    def handle(self, *args, **options):

        # print urllib2.quote('猫'.encode("utf-8"))
        # print type(urllib2.quote('猫'.encode("utf-8")))
        # txt = '猫'
        # print type(txt)
        str=u'た のしい&Python&レシピ'
        txt = urllib.quote('いろはにほへと')



        tag_recent_media, next = unauthenticated_api.tag_recent_media(tag_name='テスト')
        # tag_recent_media, next = unauthenticated_api.tag_recent_mediatag_recent_media(tag_name=u'test')
        for media in tag_recent_media:
            print media.images['standard_resolution'].url


        # tag_search, next_tag = unauthenticated_api.tag_search(q="밥")
        # tag_recent_media, next = unauthenticated_api.tag_recent_media(tag_name=tag_search[0].name)
        #
        # photos = []
        # for tag_media in tag_search:
        #     photos.append('<img src="%s"/>' % tag_media.get_standard_resolution_url())
        #     print photos

