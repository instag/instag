# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import datetime
import hashlib
from instagram_url.models import InstagramPlayer
import hmac
from hashlib import sha256
import urllib
import urlparse
import bottle
import beaker.middleware
from bottle import route, redirect, post, run, request, hook
from instagram import client, subscriptions

bottle.debug(True)

session_opts = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True,
}

INSTAGRAM_CLIENT_ID = '3dc77d748ec9434fba8d92569824b5ea'
INSTAGRAM_CLIENT_SECRET = '44dafb59c4d94095a0a326022d7e82c1'


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
        api = client.InstagramAPI(access_token='1180381936.3dc77d7.b5311ed9c8db49fda33aad54f6a05dea', client_secret=CONFIG['client_secret'])
        recent_media, next = api.user_recent_media()
        print recent_media
        
    
        
        
        