# -*- coding: utf-8 -*-
from django.db import models
from instagram_url.models import InstagramPlayer
from django.conf import settings
import datetime
import pytz
from pytz import timezone
from common import template_text as T

class FelicaTime(models.Model):
    """
    출퇴근시간 기록 테이블
    """
    id = models.AutoField(primary_key=True)
    master_user = models.ForeignKey(settings.AUTH_USER_MODEL)
    company_name = models.CharField(u'회사명', max_length=200, blank=True, null=True)
    member_name = models.CharField(u'이름', max_length=200, blank=True, null=True)
    work_time_key = models.CharField(u'work_time_key', max_length=100, blank=True, null=True)
    work_start = models.DateTimeField(u'출근', null=True)
    work_end = models.DateTimeField(u'퇴근', null=True)
    work_time_minute = models.IntegerField(u'work_time_minute', null=True)
    work_time_hour = models.IntegerField(u'work_time_hour', null=True)
    felica_id = models.CharField(u'felica_id', max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新日時', auto_now=True)

    @classmethod
    def set_work_time(cls, master_user, company_name, felica_id, member_name):
        """
        출퇴근 기록
        """
        todaydetail = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        work_time_key = str(todaydetail.year) + str(todaydetail.month) + str(todaydetail.day) + str(todaydetail.hour) + str(todaydetail.minute)
        work_record = None
        one_minute_check = None
        msg = ""
        result = None


        # 1분이내의 여러번 출퇴근을 금지하기 위해서 1분동안은 똑같은 레코드는 생성하지 않음
        try:
            one_minute_check = cls.objects.get(master_user=master_user,
                                               company_name=company_name,
                                               work_time_key=work_time_key,
                                               felica_id=felica_id)
            msg = T.CHECK_START_ERROR_MSG
        except Exception as e:
            print e

        if not one_minute_check is None: return None, msg

        try:
            # 퇴근 기록이 없는 레코드가 존재한다면 퇴근을 기록
            work_record = cls.objects.get(master_user=master_user,
                                     company_name=company_name,
                                     felica_id=felica_id,
                                     work_end=None)
            msg = T.CHECK_START_MSG
        except Exception as e:
            print e


        # 퇴근기록 경우
        if work_record:
            work_record.work_end = todaydetail
            ws = work_record.work_start.astimezone(timezone('Asia/Tokyo'))
            we = work_record.work_end

            we_all_time = (we.toordinal() * 60 * 60 * 24) + (we.hour*60*60) + (we.minute*60)
            ws_all_time = (ws.toordinal() * 60 * 60 * 24) + (ws.hour*60*60) + (ws.minute*60)

            # 총 근무한 시간 (분으로 저장)
            # print we_all_time
            # print ws_all_time
            # print (we_all_time - ws_all_time)
            # print (we_all_time - ws_all_time) / 60

            work_record.work_time_hour = ((we_all_time - ws_all_time) / 60) / 60
            work_record.work_time_minute = ((we_all_time - ws_all_time) / 60) % 60
            work_record.member_name = member_name
            work_record.save()
            msg = T.CHECK_END_MSG
            if member_name: msg = member_name + "  " + T.CHECK_END_MSG

        else:
            result, is_new = cls.objects.get_or_create(master_user=master_user,
                                                       company_name=company_name,
                                                       work_time_key=work_time_key,
                                                       felica_id=felica_id,
                                                       member_name=member_name)

            # 출근 기록
            if is_new:
                result.work_time_key = work_time_key
                result.work_start = todaydetail
                result.save()
                msg = T.CHECK_START_MSG
                if member_name: msg = member_name + "  " + T.CHECK_START_MSG

        return result, msg

    @classmethod
    def get_work_time_list(cls, wtm_start, wtm_end, felica_id):
        return cls.objects.filter(work_start__gt=wtm_start,
                                  work_end__lt=wtm_end,
                                  felica_id=felica_id)

    @classmethod
    def get_all(cls):
        try:
            return cls.objects.all()
        except:
            return None


    @classmethod
    def update(cls, user_id, post_data, id):



        result = cls.objects.get(id=id, master_user=user_id)
        result.company_name = post_data['company_name']
        result.member_name = post_data['member_name']
        if post_data['work_start']: result.work_start = post_data['work_start']
        if post_data['work_end']: result.work_end = post_data['work_end']
        if post_data['work_time_minute']:result.work_time_minute = post_data['work_time_minute']
        if post_data['work_time_hour']:result.work_time_hour = post_data['work_time_hour']
        result.felica_id = post_data['felica_id']
        result.save()
        return result


class FelicaMember(models.Model):
    """
    직원정보
    """
    id = models.AutoField(primary_key=True)
    master_user = models.ForeignKey(settings.AUTH_USER_MODEL)
    company_name = models.CharField(u'会社名', max_length=200, blank=True, null=True)
    member_name = models.CharField(u'member_name', max_length=200, blank=True, null=True, default='')
    felica_id = models.CharField(u'felica_id', max_length=200, blank=True, null=True)
    hour_price = models.IntegerField(u'hour_price', null=True, default=0)
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
    def get_member(cls, master_user, felica_id):
        """
        직원 정보 취득
        """
        return cls.objects.get(master_user=master_user,
                               felica_id=felica_id)

    @classmethod
    def get_member_list(cls, master_user):
        return cls.objects.filter(master_user=master_user)


    @classmethod
    def update(cls, user_id, post_data, id):
        result = cls.objects.get(id=id, master_user=user_id)
        result.company_name = post_data['company_name']
        result.member_name = post_data['member_name']
        if post_data['hour_price']: result.hour_price = post_data['hour_price']
        result.save()
        return result