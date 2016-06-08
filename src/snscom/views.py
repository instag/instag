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

        return response

    def post(self, request, *args, **kwargs):
        print "post_snscom"
        return HttpResponse("ok")