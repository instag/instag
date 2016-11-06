# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
import datetime

class TwitterCountJP(models.Model):
    text = models.TextField(u'본문', default='')
    body = models.TextField(u'본문', default='')
    profile_image_url = models.CharField(u'url', max_length=150, blank=True, null=True, default=None, db_index=True)
    owner = models.CharField(u'url', max_length=50, blank=True, null=True, default=None)
    uniqu_id = models.CharField(u'owner_url', max_length=50, blank=True, null=True, default=None, db_index=True)
    rtCount = models.IntegerField(u'rtCount', default=0)
    created_at = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新日時', auto_now=True)
    
class TwitterCountKO(models.Model):
    text = models.TextField(u'본문', default='')
    body = models.TextField(u'본문', default='')
    profile_image_url = models.CharField(u'url', max_length=150, blank=True, null=True, default=None, db_index=True)
    owner = models.CharField(u'url', max_length=50, blank=True, null=True, default=None)
    uniqu_id = models.CharField(u'owner_url', max_length=50, blank=True, null=True, default=None, db_index=True)
    rtCount = models.IntegerField(u'rtCount', default=0)
    created_at = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新日時', auto_now=True)
    
