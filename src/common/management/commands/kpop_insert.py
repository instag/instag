# -*- coding: utf-8 -*-
import sys

from common import template_text as T
from django.core.management.base import BaseCommand
from instagram import client
from instagram_url.models import InstagramPlayerMedia
from snscom import utils as snscom_utils


class Command(BaseCommand):
    def handle(self, *args, **options):

        # KPOP
        out = snscom_utils.get_youtube_list(snscom_utils.get_kpop_list(), 'KR', T.CACHE_KEY_KPOP_LIST, 'KR')
        result, is_new = InstagramPlayerMedia.objects.get_or_create(id=T.ID_KPOP, user_id=T.ID_KPOP)
        result.standard_resolution_url = str(out)
        result.save()

        # JPOP
        out = snscom_utils.get_youtube_list(snscom_utils.get_jpop_list(), 'JP', T.CACHE_KEY_JPOP_LIST, 'JP')
        result, is_new = InstagramPlayerMedia.objects.get_or_create(id=T.ID_JPOP, user_id=T.ID_JPOP)
        result.standard_resolution_url = str(out)
        result.save()

        #POP
        out = snscom_utils.get_youtube_list(snscom_utils.get_pop_list(), 'JP', T.CACHE_KEY_POP_LIST, 'USA')
        result, is_new = InstagramPlayerMedia.objects.get_or_create(id=T.ID_POP, user_id=T.ID_POP)
        result.standard_resolution_url = str(out)
        result.save()



