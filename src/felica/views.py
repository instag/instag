# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import calendar
import sys
from datetime import datetime as dt

from braces.views import LoginRequiredMixin
from common import template_text as T
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.views import generic
from instagram import client

from . import forms
from .models import FelicaMember, FelicaTime
from .utils import paginator_list

User = get_user_model()

reload(sys)
sys.setdefaultencoding("utf-8")

CONFIG = T.CONFIG
unauthenticated_api = client.InstagramAPI(**CONFIG)

class Felica(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        # 가게의 마스터 데이터가 있는지 확인
        master_user = User.objects.get(name=request.GET['company_name'])

        if master_user:
            # 직원데이터 생성 및 취득
            fm = FelicaMember.get_or_create_member(master_user,
                                                   master_user.name,
                                                   request.GET['felica_id'])

            # 퇴근 기록
            fswt, msg = FelicaTime.set_work_time(master_user,
                                            master_user.name,
                                            request.GET['felica_id'],
                                            fm.member_name)

            return HttpResponse(msg, status=200)

        return HttpResponse('Error', status=200)


    def post(self, request, *args, **kwargs):
        print "felica...2"
        # return HttpResponse("ok")



class FelicaMemberEdit(LoginRequiredMixin, generic.TemplateView):

    template_name = "felica/felica_member_edit.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        print "edit...felica.get"
        user = self.request.user
        felica_member = FelicaMember.objects.get(id=kwargs['id'], master_user=user.id)
        kwargs["felica_member_form"] = forms.FelicaMemberForm(instance=felica_member)
        return super(FelicaMemberEdit, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print "edit...felica.post"
        user = self.request.user
        result = FelicaMember.update(user.id, request.POST, kwargs['id'])
        messages.success(request, " details saved!")
        return redirect("felica:felica_member_list")


class FelicaWorkTime(LoginRequiredMixin, generic.TemplateView):
    template_name = "felica/felica_work_time.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):

        if request.GET.get('bdaymonth') and request.GET.get('select_member_felica_id'):
            wtm_start = dt.strptime('%s-01 00:00:00' % request.GET.get('bdaymonth'), '%Y-%m-%d %H:%M:%S')

            member = FelicaMember.get_member(self.request.user, request.GET.get('select_member_felica_id'))

            # 월별 총 일수
            f_total_hour = 0
            f_total_minute = 0
            total_days = calendar.monthrange(wtm_start.year,wtm_start.month)[1]
            wtm_end = dt.strptime('%s-%s 23:59:59' % (request.GET.get('bdaymonth'), str(total_days)), '%Y-%m-%d %H:%M:%S')
            ft_list = FelicaTime.get_work_time_list(wtm_start, wtm_end, request.GET.get('select_member_felica_id'))

            work_time = paginator_list(ft_list,request.GET.get('page', 1),T.PAGE_COUNT)


            for f in ft_list:
                if f.work_time_hour: f_total_hour =+ f.work_time_hour
                if f.work_time_minute: f_total_minute =+ f.work_time_minute

            return render(request, 'felica/felica_work_time.html',
                          {'work_time': work_time,
                           'member': member,
                           'f_total_hour': f_total_hour,
                           'f_total_minute': f_total_minute,
                           'month': request.GET.get('bdaymonth'),
                           'member_list': FelicaMember.get_member_list(self.request.user)})



        work_time = paginator_list(FelicaTime.get_all(), request.GET.get('page', 1), T.PAGE_COUNT)
        return render(request, 'felica/felica_work_time.html', {'work_time': work_time,
                                                                'member_list': FelicaMember.get_member_list(self.request.user)})


class FelicaTimeEdit(LoginRequiredMixin, generic.TemplateView):

    template_name = "felica/felica_time_edit.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        felica_time = FelicaTime.objects.get(id=kwargs['id'], master_user=user.id)
        kwargs["felica_time_form"] = forms.FelicaTimeForm(instance=felica_time)
        return super(FelicaTimeEdit, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        result = FelicaTime.update(user.id, request.POST, kwargs['id'])
        messages.success(request, " work time saved!")
        return redirect("felica:felica_work_time")


class FelicaMemberList(LoginRequiredMixin, generic.TemplateView):
    template_name = "felica/felica_member_list.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return render(request, 'felica/felica_member_list.html', {'member_list': FelicaMember.get_member_list(self.request.user)})


