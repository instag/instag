# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from django.conf.settings import settings
import datetime
import hashlib
# from bootcamp.twits.models import Twit

INSTAGRAM_CLIENT_ID = '3dc77d748ec9434fba8d92569824b5ea'
INSTAGRAM_CLIENT_SECRET = '44dafb59c4d94095a0a326022d7e82c1'

class Command(BaseCommand):
    """
    instagramからimgを取得する
    """
    def handle(self, *args, **options):
        