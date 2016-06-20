# -*- coding: utf-8 -*-
from common import template_text as T
from django.core.management.base import BaseCommand
from instagram import client
from minsta.models import Tag
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
        for t in Tag.objects.filter(tag_flg="1"):
            # try :

            user_search = unauthenticated_api.user_search(q="orange3311")
            users = []
            for user in user_search:
                print user.profile_picture
                print user.username

                    # users.append('<li><img src="%s">%s</li>' % (user.profile_picture,user.username))


            #     tag_recent_media, next = unauthenticated_api.tag_recent_media(tag_name=t.tag)
            #     for media in tag_recent_media:
            #
            #         # 스팸으로 인해 최소한 좋아요 클릭수가 20이상의 사진만을 취득함
            #         if media.like_count > 0:
            #             print media
            #             result, is_new = InstagramPlayerMedia.objects.get_or_create(user_id=1, media_id=media.id)
            #             if is_new:
            #                 result.low_resolution_url = media.get_low_resolution_url()
            #                 result.standard_resolution_url = media.get_standard_resolution_url()
            #                 result.thumbnail_url = media.get_thumbnail_url()
            #                 result.media_link = media.link
            #                 result.media_type = media.type
            #                 result.caption = media.caption.text[1:100]
            #                 result.like_count = media.like_count
            #                 result.comment_count = media.comment_count
            #                 result.tags = t.tag
            #                 result.save()
            # except Exception as e:
            #     print "[ERROR]  %s" % e
