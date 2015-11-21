# # -*- coding: utf-8 -*-
# 
# from __future__ import absolute_import
# 
# from django.conf import settings
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render_to_response
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
# from django.template import RequestContext
# import datetime
# from django.core.cache import cache
# from instagram_url import api as in_api
# from opensocial.http import HttpResponseOpensocialRedirect
# from instagram.client import InstagramAPI
# import os
# import urllib
# import urllib2
# from survey.forms import MessageApiForm
# from survey import message_sender
# import logging 
# import json
# from instagram_url.models import InstagramPlayer
# 
# from django.core import serializers
# from django.http import HttpResponse, HttpResponseNotFound
# 
# 
# 
# # configure Instagram API
# #instaConfig = {
# #    'client_id':os.environ.get('1fcb56b538474f8c9131b8eb8ec213f9'),
# #    'client_secret':os.environ.get('8f114a00e6f24cc4a2a5f6510113e741'),
# #    'redirect_uri' : os.environ.get('http://localhost:5000/survey/instagram/index/')
# #}
# #api = InstagramAPI(**instaConfig)
# 
# #access_token = "1180381936.1fcb56b.ab48f49d327144dfb21999b979f2fdc1"
# client_id = "1fcb56b538474f8c9131b8eb8ec213f9"
# client_secret = "8f114a00e6f24cc4a2a5f6510113e741"
# #redirect_uri = "http://localhost:5000/survey/instagram/index/"
# #redirect_uri = "http://waku-dev.pairon-battle.jp/survey/instagram/index/"
# redirect_uri = "http://dev.followkr.com/survey/instagram/index/"
# 
# #api = InstagramAPI(access_token=access_token)
# api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
# 
# def instagram_delete(request):
#     InstagramPlayer.objects.all().delete()
#     return HttpResponseOpensocialRedirect(reverse('instagram/index'))
#     
#     
#     
# def instagram_logout(request):
#     request.session['access_token'] = None
#     request.session.clear()
#     return HttpResponseRedirect(reverse('instagram/index'))
# #    return HttpResponseRedirect(reverse('http://instagram.com/accounts/logout/'))
# #    return HttpResponseRedirect('http://instagram.com/accounts/logout/')
# #    return HttpResponseRedirect(reverse('http://yahoo.co.jp'))
# #    return render_to_response('http://yahoo.co.jp')
# #    return HttpResponseRedirect(reverse('survey/invite/invite'))
#     
# #@login_required
# def instagram_index(request):    
#     code = request.GET.get('code')
#     url = None
#     access_token = None
#     in_player = None
# 
#     if code:
#         try:
#             url = api.get_authorize_url(scope=["relationships"])
#             access_token, user = api.exchange_code_for_access_token(code)
#             request.session['access_token'] = access_token
#             
#             if user:
#                 in_player = in_api.get_instagram_player(user, code, access_token)
#         except:
#             pass
#     else:
#         access_token = request.session.get('access_token',None)
#         in_player = in_api.get_instagram_player_token(access_token)
#     
#     tag_1 = request.POST.get('tag1')
#     tag_2 = request.POST.get('tag2')
#     tag_3 = request.POST.get('tag3')
#     tag_4 = request.POST.get('tag4')
#     tag_5 = request.POST.get('tag5')
#     tag_6 = request.POST.get('tag6')
#     
# #    print tag_1, tag_2, tag_3, tag_4, tag_5, tag_6
#     if tag_1 or tag_2 or tag_3 or tag_4 or tag_5 or tag_6:
#         in_player = in_api.set_tag(access_token, tag_1, tag_2, tag_3, tag_4, tag_5, tag_6)
#     
#     
#     ctxt = RequestContext(request, {
#         'request' : request,
#         'code' : code,
#         'in_player' : in_player,
#         'url' : url,
# #        'tag1' : tag1,
# #        'tag2' : tag2,
# #        'tag3' : tag3,
# #        'user_id' : user_id,
# #        'user_name' : user_name,
#         'redirect_uri' : redirect_uri,
#         'client_id' : client_id,
#         'access_token' : access_token,
# #        'profile_picture' : profile_picture,
#     })
#     return render_to_response('survey/twitter_url/instagram_index.html', ctxt)