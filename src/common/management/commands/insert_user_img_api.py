# -*- coding: utf-8 -*-
import beaker.middleware
import bottle
from django.core.management.base import BaseCommand
from instagram import client
from instagram_url.models import InstagramPlayer
from common import template_text as T

bottle.debug(True)
CONFIG = T.CONFIG

app = beaker.middleware.SessionMiddleware(bottle.app(), T.session_opts)
unauthenticated_api = client.InstagramAPI(**CONFIG)

class Command(BaseCommand):
    """
    instagramからimgを取得する
    """

    def handle(self, *args, **options):

        for i in InstagramPlayer.objects.all():
            api = client.InstagramAPI(access_token=i.oauth_token, client_secret=CONFIG['client_secret'])
            recent_media, next = api.user_recent_media()
            for media in recent_media:
                print media.get_low_resolution_url()
                print media.tags



