# -*- coding: utf-8 -*-
from django.db import models
from instagram_url.models import InstagramPlayer
from django.conf import settings

class FelicaTime(models.Model):
    """
    출퇴근시간 기록 테이블
    """
    master_user = models.OneToOneField(settings.AUTH_USER_MODEL,primary_key=True)
    company_name = models.CharField(u'会社名', max_length=200, blank=True, null=True)
    member_name = models.CharField(u'会社名', max_length=200, blank=True, null=True)
    work_start = models.DateTimeField(u'work_start', auto_now_add=True)
    work_end = models.DateTimeField(u'work_end', auto_now_add=True)
    felica_id = models.CharField(u'felica_id', max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新日時', auto_now=True)

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


class FelicaMember(models.Model):
    """
    직원정보
    """
    master_user = models.OneToOneField(settings.AUTH_USER_MODEL,primary_key=True)
    company_name = models.CharField(u'会社名', max_length=200, blank=True, null=True)
    member_name = models.CharField(u'member_name', max_length=200, blank=True, null=True)
    felica_id = models.CharField(u'member_name', max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新日時', auto_now=True)

    @classmethod
    def get_or_create_member(cls, master_user, company_name, felica_id):
        """
        직원 정보 취득 없으면 생성
        """
        print master_user
        print company_name
        print felica_id

        print "9999999"
        result, is_new = cls.objects.get_or_create(master_user=master_user, company_name=company_name, felica_id=felica_id)
        print 111
        # print is_new
        # print result

        # result.save()

    @classmethod
    def get_member_list(cls, master_user):
        return cls.objects.filter(master_user=master_user)