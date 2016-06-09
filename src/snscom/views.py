# -*- coding: utf-8 -*-
import sys
from common import template_text as T
from django.http import HttpResponse
from django.views import generic
from instagram import client

reload(sys)
sys.setdefaultencoding("utf-8")
import json

CONFIG = T.CONFIG
unauthenticated_api = client.InstagramAPI(**CONFIG)


class Snscom(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        print "get_snscom"
        response = HttpResponse(json.dumps({'test':'test_value'}), content_type="application/json", status=200)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'

        return response.GET
        return response.POST

    def post(self, request, *args, **kwargs):
        print "post_snscom"
        return HttpResponse("ok")

class Profile(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        print "get_profile"
        print args
        print kwargs
        print request.GET
        print request.body

        response = HttpResponse(json.dumps({'test':'test_value'}), content_type="application/json", status=200)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'

        return response

    def post(self, request, *args, **kwargs):
        print "post_profile"
        return HttpResponse("ok")

