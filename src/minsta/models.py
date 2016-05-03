# -*- coding: utf-8 -*-
from django.db import models


class Instagram(models.Model):
    access_token = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    user_id = models.IntegerField()
    full_name = models.CharField(max_length=255)
    
    @classmethod
    def get_or_create_user(cls, access_token, username, user_id):
        result = Instagram.objects.get_or_create(user_id=user_id)[0]
        result.access_token = access_token
        result.username = username
        result.full_name = username
        result.user_id = user_id
        result.save()
        return result
        

class Tag(models.Model):
    tag = models.CharField(max_length=255)
    tag_flg = models.IntegerField(u'tag_flg', default=0, db_index=True)
    created_at = models.DateTimeField(u'작성 일자', auto_now_add=True)
    updated_at = models.DateTimeField(u'갱신 일자', auto_now=True)

    def __unicode__(self):
        return self.tag


class Media(models.Model):
    media_id = models.CharField(max_length=255)
    allowed = models.BooleanField()

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media'
