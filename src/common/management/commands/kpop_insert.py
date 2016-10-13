# -*- coding: utf-8 -*-
import sys

from common import template_text as T
from django.core.management.base import BaseCommand
from instagram import client
from instagram_url.models import InstagramPlayerMedia
from snscom import utils as snscom_utils
import json


class Command(BaseCommand):
    def handle(self, *args, **options):

        # KPOP
        k_count = 100
        InstagramPlayerMedia.objects.all().delete()
        kpop_list = snscom_utils.get_youtube_list(snscom_utils.get_kpop_list(), 'KR', T.CACHE_KEY_KPOP_LIST, 'KR')
        for k in kpop_list:
            result, is_new = InstagramPlayerMedia.objects.get_or_create(id=k_count, user_id=k_count)
            result.media_type = 'KPOP'
            result.standard_resolution_url = json.dumps(k, ensure_ascii=False)
            result.save()
            k_count = k_count + 1

        # JPOP
        j_count = 200
        jpop_list = snscom_utils.get_youtube_list(snscom_utils.get_jpop_list(), 'JP', T.CACHE_KEY_JPOP_LIST, 'JP')
        for j in jpop_list:
            result, is_new = InstagramPlayerMedia.objects.get_or_create(id=j_count, user_id=j_count)
            result.media_type = 'JPOP'
            result.standard_resolution_url = json.dumps(j, ensure_ascii=False)
            result.save()
            j_count = j_count + 1


        #POP
        pop_count = 300
        pop_list = snscom_utils.get_youtube_list(snscom_utils.get_pop_list(), 'JP', T.CACHE_KEY_POP_LIST, 'USA')
        for p in pop_list:
            result, is_new = InstagramPlayerMedia.objects.get_or_create(id=pop_count, user_id=pop_count)
            result.media_type = 'POP'
            result.standard_resolution_url = json.dumps(p, ensure_ascii=False)
            result.save()
            pop_count = pop_count + 1


