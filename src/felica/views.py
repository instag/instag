# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from braces.views import LoginRequiredMixin
import sys
from django.shortcuts import render, redirect, get_object_or_404
from common import template_text as T
from django.views import generic
from instagram import client
from profile import Profile
from .models import FelicaMember, FelicaTime
from . import forms
from django.contrib import messages
from django.shortcuts import redirect

from django.contrib.auth import get_user_model
User = get_user_model()


reload(sys)
sys.setdefaultencoding("utf-8")

CONFIG = T.CONFIG
unauthenticated_api = client.InstagramAPI(**CONFIG)

class Felica(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        print "felica.....11111"
        # 가게의 마스터 데이터가 있는지 확인
        master_user = User.objects.get(name=request.GET['company_name'])

        if master_user:
            # 직원데이터 생성 및 취득
            fm = FelicaMember.get_or_create_member(master_user,
                                                   master_user.name,
                                                   request.GET['felica_id'])

            # 퇴근 기록
            fswt = FelicaTime.set_work_time(master_user,
                                            master_user.name,
                                            request.GET['felica_id'])


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

        print request.GET
        if request.GET.get('bdaymonth'):

            from datetime import datetime as dt
            import calendar
            wtm_start = dt.strptime('%s-01 00:00:00' % request.GET.get('bdaymonth'), '%Y-%m-%d %H:%M:%S')

            # 월별 총 일수
            total_days = calendar.monthrange(wtm_start.year,wtm_start.month)[1]
            wtm_end = dt.strptime('%s-%s 23:59:59' % (request.GET.get('bdaymonth'), str(total_days)), '%Y-%m-%d %H:%M:%S')

            return render(request, 'felica/felica_work_time.html',
                          {'work_time': FelicaTime.get_work_time_list(wtm_start, wtm_end),
                           'member_list': FelicaMember.get_member_list(self.request.user)})

        return render(request, 'felica/felica_work_time.html', {'work_time': FelicaTime.get_all(),
                                                                'member_list': FelicaMember.get_member_list(self.request.user)})


class FelicaMemberList(LoginRequiredMixin, generic.TemplateView):
    template_name = "felica/felica_member_list.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return render(request, 'felica/felica_member_list.html', {'member_list': FelicaMember.get_member_list(self.request.user)})


