# -*- coding: utf-8 -*-
from django.db import models
from instagram_url.models import InstagramPlayer
from django.conf import settings
import datetime

class FelicaTime(models.Model):
    """
    출퇴근시간 기록 테이블
    """
    id = models.AutoField(primary_key=True)
    master_user = models.ForeignKey(settings.AUTH_USER_MODEL)
    company_name = models.CharField(u'会社名', max_length=200, blank=True, null=True)
    member_name = models.CharField(u'会社名', max_length=200, blank=True, null=True)
    work_time_key = models.CharField(u'work_time_key', max_length=100, blank=True, null=True)
    work_start = models.DateTimeField(u'work_start', null=True)
    work_end = models.DateTimeField(u'work_end', null=True)
    felica_id = models.CharField(u'felica_id', max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新日時', auto_now=True)

    @classmethod
    def set_work_time(cls, master_user, company_name, felica_id):
        """
        출퇴근 기록
        """
        todaydetail = datetime.datetime.today()
        work_time_key = str(todaydetail.year) + str(todaydetail.month) + str(todaydetail.day) + str(todaydetail.hour) + str(todaydetail.minute)
        work_record = None
        one_minuts_check = None

        # 1분이내의 여러번 출퇴근을 금지하기 위해서 1분동안은 똑같은 레코드는 생성하지 않음
        try:
            one_minuts_check = cls.objects.get(master_user=master_user,
                                               company_name=company_name,
                                               work_time_key=work_time_key,
                                               felica_id=felica_id)
        except Exception as e:
            print e

        if not one_minuts_check is None: return None
        print "true...."
        try:
            # 퇴근 기록이 없는 레코드가 존재한다면 퇴근을 기록
            work_record = cls.objects.get(master_user=master_user,
                                     company_name=company_name,
                                     felica_id=felica_id,
                                     work_end=None)
        except Exception as e:
            print e


        # 퇴근기록 경우
        if work_record:
            work_record.work_end = datetime.datetime.now()
            work_record.save()
        else:
            result, is_new = cls.objects.get_or_create(master_user=master_user,
                                                       company_name=company_name,
                                                       work_time_key=work_time_key,
                                                       felica_id=felica_id)

            # 출근 기록
            if is_new:
                result.work_time_key = work_time_key
                result.work_start = datetime.datetime.now()
                result.save()

        return result

    @classmethod
    def get_work_time_list(cls, wtm_start, wtm_end):

        print wtm_start
        print wtm_end

        return cls.objects.filter(work_start__gt=wtm_start, work_end__lt=wtm_end)

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
    id = models.AutoField(primary_key=True)
    master_user = models.ForeignKey(settings.AUTH_USER_MODEL)
    company_name = models.CharField(u'会社名', max_length=200, blank=True, null=True)
    member_name = models.CharField(u'member_name', max_length=200, blank=True, null=True, default='')
    felica_id = models.CharField(u'member_name', max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新日時', auto_now=True)

    @classmethod
    def get_or_create_member(cls, master_user, company_name, felica_id):
        """
        직원 정보 취득 없으면 생성
        """
        try:
            result, is_new = cls.objects.get_or_create(master_user=master_user,
                                                                company_name=company_name,
                                                                felica_id=felica_id)
        except Exception as e:
            print e

        return result

    @classmethod
    def get_member_list(cls, master_user):
        return cls.objects.filter(master_user=master_user)


    @classmethod
    def update(cls, user_id, post_data, id):
        result = cls.objects.get(id=id, master_user=user_id)
        result.company_name = post_data['company_name']
        result.member_name = post_data['member_name']
        result.save()
        return result