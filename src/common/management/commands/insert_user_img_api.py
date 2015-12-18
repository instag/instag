# -*- coding: utf-8 -*-
import beaker.middleware
import bottle
from django.core.management.base import BaseCommand
from instagram import client
from instagram_url.models import InstagramPlayer

bottle.debug(True)

session_opts = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True,
}

app = beaker.middleware.SessionMiddleware(bottle.app(), session_opts)

CONFIG = {
    'client_id': '3dc77d748ec9434fba8d92569824b5ea',
    'client_secret': '44dafb59c4d94095a0a326022d7e82c1',
    'redirect_uri': 'http://localhost:8515/oauth_callback'
}

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



