# -*- coding: utf-8 -*-
from __future__ import absolute_import
import datetime
import json
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views import generic
from instagram.client import InstagramAPI
from twitter_count.models import TwitterCountJP, TwitterCountKO

#access_token = "1180381936.1fcb56b.ab48f49d327144dfb21999b979f2fdc1"
client_id = "1fcb56b538474f8c9131b8eb8ec213f9"
client_secret = "8f114a00e6f24cc4a2a5f6510113e741"
redirect_uri = "http://localhost:5000/survey/instagram/index/"

#api = InstagramAPI(access_token=access_token)
api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

REAL_TIME = 12
HOT_TIME = 11
TODAY_TIME = 34
#몇건 보여줄건지
VIEW_LIST_CNT = 10
#메인 보여줄 건수
VIEW_LIST_MAIN_CNT = 5


class RealtimeJP(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        """
        최근 2시간동안의 인기 트윗만
        """
        json_list = []
        entrys = []
        rank_count = 0
        now = datetime.datetime.now()
        limit_time = now - datetime.timedelta(hours=REAL_TIME)
        url_to = request.REQUEST.get('to','100')
        url_from = request.REQUEST.get('from','1')

        CACHE_KEY = 'twitter::jp::api::%s' % (url_to)
        out = cache.get(CACHE_KEY, None)

        if out is None:
    #     if True:
            twitter_ranking_list = TwitterCountJP.objects.filter(created_at__gte=limit_time).order_by('-rtCount')[:url_to]
            twitter_ranking_list = twitter_ranking_list[int(url_from)-1:url_to]
            for t in twitter_ranking_list:
                json_dic = {"id":t.uniqu_id,
                            "ownerProfileImgUrl":t.profile_image_url, "owner":t.owner,  "body":t.body, "rtRank":url_from, "rtCount":t.rtCount, "registDate":t.created_at.strftime("%Y/%m/%d %H:%M:%S"),  "rtTwitCount":0, "twitId":0}
                url_from = int(url_from) + 1
                json_list.append(json_dic)

            entrys.append(json.dumps({"rankedTwitList":json_list}))
            cache.set(CACHE_KEY, entrys, 900) # 15분 동안 캐쉬
            return HttpResponse(entrys, content_type='text/plain')
        return HttpResponse(out, content_type='text/plain')
        ctxt = RequestContext(request, {'tag' : tag,})
        return render_to_response('survey/twitter_url/api.html', ctxt)

class RealtimeKO(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        """
        최근 2시간동안의 인기 트윗만
        """
        json_list = []
        entrys = []
        rank_count = 0
        now = datetime.datetime.now()
        limit_time = now - datetime.timedelta(hours=REAL_TIME)
        url_to = request.REQUEST.get('to','100')
        url_from = request.REQUEST.get('from','1')
        CACHE_KEY = 'twitter::ko::api::%s' % ( url_to)
        out = cache.get(CACHE_KEY, None)
        if out is None:
    #     if True:
            twitter_ranking_list = TwitterCountKO.objects.filter(created_at__gte=limit_time).order_by('-rtCount')[:url_to]
            twitter_ranking_list = twitter_ranking_list[int(url_from)-1:url_to]

            for t in twitter_ranking_list:
                json_dic = {"id":t.uniqu_id, "ownerProfileImgUrl":t.profile_image_url, "owner":t.owner,  "body":t.body, "rtRank":url_from, "rtCount":t.rtCount, "registDate":t.created_at.strftime("%Y/%m/%d %H:%M:%S"),  "rtTwitCount":0, "twitId":0}
                url_from = int(url_from) + 1
                json_list.append(json_dic)
            entrys.append(json.dumps({"rankedTwitList":json_list}))
            cache.set(CACHE_KEY, entrys, 900) # 15분 동안 캐쉬
            return HttpResponse(entrys, content_type='text/plain')
        return HttpResponse(out, content_type='text/plain')
        ctxt = RequestContext(request, {'tag' : tag,})
        return render_to_response('survey/twitter_url/api.html', ctxt)
