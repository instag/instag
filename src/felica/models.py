# -*- coding: utf-8 -*-
from django.db import models
from instagram_url.models import InstagramPlayer


class Felica(models.Model):
    user = models.ForeignKey(InstagramPlayer)
    shop_title = models.CharField(u"SHOP 이름", max_length=200, blank=True, null=True)
    shop_description = models.TextField(u"SHOP 소개", default='')

    @classmethod
    def get_or_create(cls, user_id):
        instagramplayer = InstagramPlayer.get_instagram_play(user_id)
        result, is_new = cls.objects.get_or_create(user=instagramplayer)

        return result

    @classmethod
    def get_all(cls):
        try:
            return cls.objects.all()
        except:
            return None