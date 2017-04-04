# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from braces.views import LoginRequiredMixin
import sys
from django.shortcuts import render, redirect, get_object_or_404
from common import template_text as T
from django.views import generic
from instagram import client
from profile import Profile
from .models import FelicaMember

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
        print request.GET['company_name']
        master_user = User.objects.get(name=request.GET['company_name'])
        if master_user:
            # 직원데이터 생성 및 취득
            print 44
            FelicaMember.get_or_create_member(master_user,
                                            master_user.name,
                                            request.GET['company_name'])

    def post(self, request, *args, **kwargs):
        print "felica...2"
        # return HttpResponse("ok")



class FelicaMemberList(LoginRequiredMixin, generic.TemplateView):
    template_name = "felica/felica_member_list.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        print 1111111

        # if request.GET.get('bdaymonth'):
        #     tstr_start = request.GET.get('bdaymonth') + '-01 00:00:00'
        #     tdatetime_start = dt.strptime(tstr_start, '%Y-%m-%d %H:%M:%S')
        #     tdatetime_end = dt.strptime(str(last_day_of_month(datetime.date(tdatetime_start.year, tdatetime_start.month, 1))) + ' 23:59:59', '%Y-%m-%d %H:%M:%S')
        #     result_shop = Shop.get_shop_by_user(self.request.user, tdatetime_start, tdatetime_end)
        #     kwargs["shop_list"] = paginator_list(result_shop, request.GET.get('page', 1), T.PAGE_COUNT)
        # else:
        #     result_shop = Shop.get_shop_by_user(self.request.user)
        #     kwargs["shop_list"] = paginator_list(result_shop, request.GET.get('page', 1), T.PAGE_COUNT)

        print FelicaMember.get_member_list(self.request.user)

        # FelicaMember.get_or_create_member(master_user,
        #                                     master_user.name,
        #                                     request.GET['company_name'])


        # kwargs["sales"], kwargs["a1"], kwargs["a2"], kwargs["a3"] = Shop.get_total_list(result_shop)
        # return super(FelicaMemberList, self).get(request, *args, **kwargs)
        return render(request, 'felica/felica_member_list.html', {'member_list': FelicaMember.get_member_list(self.request.user)})


