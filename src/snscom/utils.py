# -*- coding: utf-8 -*-
import sys
import urllib2
from common import template_text as T
from instagram import client
from django.core.cache import cache

reload(sys)
sys.setdefaultencoding("utf-8")
import json
import time, datetime
import feedparser
from apiclient.discovery import build
from django.core.cache import cache
from django.http import HttpResponse

CONFIG = T.CONFIG
unauthenticated_api = client.InstagramAPI(**CONFIG)


TOP_100_KR_COUNT = 100
TOP_100_JP_COUNT = 100
IS_NEW_SONG_DAYS_JPOP = 10

DEVELOPER_KEY = "AIzaSyAcwCMEw4IWmUalZSEG1SGXpMnMAcdcLKA"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_kpop_list():
    APP_KEY = "8130bcbd-c523-3e5e-9d88-902707794ee4"
    PAGE = 1
    VERSION = 1
    y_list = []
    headers = {'appkey': APP_KEY,
               'access_token': '',
               'Accept-Languag': 'ko_KR'
               }

    song_list = cache.get(T.CACHE_KEY_K_POP_TITLE_LIST, None)
    if song_list is None:

        url = 'http://apis.skplanetx.com/melon/charts/todaytopsongs?count=%d&page=%d&version=%d' % \
              (TOP_100_KR_COUNT, PAGE, VERSION)
        req = urllib2.Request(url, None, headers)

        # Read the response
        resp = urllib2.urlopen(req).read()
        data = json.loads(resp.decode('utf8')).get("melon", [])

        for d in data['songs'].iteritems():
            for s in d[1]:
                dict_list = {}
                dict_list['title'] = s['songName']
                dict_list['name'] = s['artists']['artist'][0]['artistName']
                title = s['songName'] + " " + s['artists']['artist'][0]['artistName']
                dict_list['is_new'] = ""
                if s['pastRank'] == 0:
                    dict_list['is_new'] = "NEW"
                y_list.append(dict_list)

        cache.set(T.CACHE_KEY_K_POP_TITLE_LIST, y_list, T.CACHE_TIME)
        song_list = y_list

    return song_list


def get_jpop_list():

        y_list = []
        """
        1건일때하고 1건 이상일때 리턴 형식이 들려짐..
        """
        url = 'https://itunes.apple.com/jp/rss/topsongs/limit=%d/json' % TOP_100_JP_COUNT
        r = urllib2.urlopen(url)
        result = json.loads(r.read())

        song_list = cache.get(T.CACHE_KEY_J_POP_TITLE_LIST, None)

        if song_list is None:
            for r in result.iteritems():
                for e in r[1]['entry']:

                    dict_list = {}
                    dict_list['title'] = e['title']['label']
                    dict_list['name'] = e['im:artist']['label']
                    is_new_temp = str(e['im:releaseDate']['label'])
                    dict_list['is_new'] = ""
                    try:
                        release_date = datetime.datetime(int(is_new_temp[0:4]), int(is_new_temp[5:7]), int(is_new_temp[8:10]), 00, 00, 00, 000000)
                        today = datetime.date.today()
                        days = datetime.timedelta(days=IS_NEW_SONG_DAYS_JPOP)
                        old_day = today - days
                        if release_date.date() > old_day:
                            dict_list['is_new'] = "NEW"
                    except:
                        pass
                    y_list.append(dict_list)
            cache.set(T.CACHE_KEY_J_POP_TITLE_LIST, y_list, T.CACHE_TIME)
            song_list = y_list

        return song_list

def get_pop_list():
    y_list = []
    song_list = cache.get(T.CACHE_KEY_POP_TITLE_LIST, None)

    if song_list is None:
        url  = 'http://www.billboard.com/rss/charts/hot-100'
        data = feedparser.parse(url)
        for entry in data['entries']:
            dict_list = {}
            dict_list['is_new'] = ""
            if entry['rank_last_week'] == '0':
                dict_list['is_new'] = "NEW"
            dict_list['title'] = entry['chart_item_title']
            dict_list['name'] = entry['artist']
            y_list.append(dict_list)
        cache.set(T.CACHE_KEY_POP_TITLE_LIST, y_list, T.CACHE_TIME)
        song_list = y_list

    return song_list


def get_youtube_list(title_list, regionCode, CACHE_KEY, country):

        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
        json_list = []
        count = 0
        rank = 1
        for t in title_list:
            if country == 'KR' or country == 'USA':
                search_q = t['title'] + " " + t['name']
            else:
                search_q = t['title']

            search_response = youtube.search().list(
            q=search_q,
            regionCode=regionCode,
            order="relevance",
            part="id,snippet",
            type="video",
            safeSearch="moderate",
            maxResults=1
            ).execute()

            for search_result in search_response.get("items", []):
                if search_result["id"]["kind"] == "youtube#video":
                    json_dic = {
                                "id":count,
                                "rank":rank,
                                "videoId":search_result["id"]["videoId"],
                                "title":t['title'],
                                "name":t['name'],
                                "is_new":t['is_new'],
                                "img":search_result["snippet"]["thumbnails"]["default"]["url"],
                                "thumbnail_url":search_result["snippet"]["thumbnails"]["default"]["url"],
                                "url": 'http://m.youtube.com/watch?v=%s' % search_result["id"]["videoId"]
                               }
                    json_list.append(json_dic)
            count = count + 1
            rank = rank + 1
        cache.set(CACHE_KEY, json_list, T.CACHE_TIME)

        return json_list



def get_response(out):
    response = HttpResponse(json.dumps(out), content_type="application/json", status=200)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response
