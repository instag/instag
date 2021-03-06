# -*- coding: utf-8 -*-
from common import template_text as T
from django.core.management.base import BaseCommand
from instagram import client
from instagram_url.models import InstagramPlayer, InstagramPlayerMedia

CONFIG = T.CONFIG
unauthenticated_api = client.InstagramAPI(**CONFIG)

class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in InstagramPlayer.objects.all():
            api = client.InstagramAPI(access_token=i.oauth_token, client_secret=CONFIG['client_secret'])
            recent_media, next = api.user_recent_media()
            for media in recent_media:
                for k in media.tags:
                    if k.name == T.WISHTAG:
                        result, is_new = InstagramPlayerMedia.objects.get_or_create(user=i, media_id=media.id)
                        if is_new:
                            result.low_resolution_url = media.get_low_resolution_url()
                            result.standard_resolution_url = media.get_standard_resolution_url()
                            result.thumbnail_url = media.get_thumbnail_url()
                            result.media_link = media.link
                            result.media_type = media.type
                            result.caption = media.caption.text
                            result.tags = str(media.tags)
                            result.save()
