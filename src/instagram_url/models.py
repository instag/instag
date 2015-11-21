# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
import datetime

class InstagramPlayer(models.Model):
    user_id = models.IntegerField(u'uer_id', default=0, db_index=True)
    user_name = models.CharField(u'user_name', max_length=100, default="")
    user_site_id = models.IntegerField(u'uer_id', default=0)
    code = models.TextField(u'code', default='')
    media_cnt = models.IntegerField(u'media_cnt', default=0, db_index=True)
    followed_by = models.IntegerField(u'followed_by', default=0, db_index=True)
    follows = models.IntegerField(u'follows', default=0, db_index=True)
    tag_1 = models.CharField(u'tag_1', max_length=100, default="")
    tag_2 = models.CharField(u'tag_2', max_length=100, default="")
    tag_3 = models.CharField(u'tag_3', max_length=100, default="")
    tag_4 = models.CharField(u'tag_4', max_length=100, default="")
    tag_5 = models.CharField(u'tag_5', max_length=100, default="")
    tag_6 = models.CharField(u'tag_6', max_length=100, default="")
    follow_total = models.IntegerField(u'follow_total', default=0, db_index=True)
    like_total = models.IntegerField(u'like_total', default=0, db_index=True)
    point = models.IntegerField(u'point', default=100, db_index=True)
    oauth_token = models.TextField(u'oauth_token', default='')
    profile_picture = models.TextField(u'profile_picture', default='')
    relation_flg = models.IntegerField(u'relation_flg', default=0, db_index=True)
    created_at = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新日時', auto_now=True)

class InstagramPlayerFollowHistory(models.Model):
    user_id = models.IntegerField(u'uer_id', default=0, db_index=True)
    target_id = models.IntegerField(u'target_id', default=0, db_index=True)
    created_at = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新日時', auto_now=True)