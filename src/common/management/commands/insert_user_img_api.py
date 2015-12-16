# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import datetime
import hashlib
from instagram_url.models import InstagramPlayer
from instagram.client import InstagramAPI

# from bootcamp.twits.models import Twit

INSTAGRAM_CLIENT_ID = '3dc77d748ec9434fba8d92569824b5ea'
INSTAGRAM_CLIENT_SECRET = '44dafb59c4d94095a0a326022d7e82c1'

class Command(BaseCommand):
    """
    instagramからimgを取得する
    """
    def handle(self, *args, **options):
        
            instagram = InstagramPlayer.objects.all()[0]
            print type(instagram)
            
            print instagram.oauth_token
            print instagram.user_id
            api = InstagramAPI(access_token=instagram.oauth_token)
            media, discard = api.user_recent_media(user_id=instagram.user_id, count=24)
#             try:
#             except InstagramAPIError as e:
#                 logger.error(e)
#                 return {"media": []}
#             return {"media": media}
#         except IndexError:
#             return {"media": []}
#         
        