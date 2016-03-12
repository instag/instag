# -*- coding:utf-8 -*-
from django.conf import settings
import datetime
from .hostname import HOSTNAME

WISHTAG = 'wishtag'

if HOSTNAME.startswith('wishtag.net'):
    CONFIG = {
        'client_id': '3dc77d748ec9434fba8d92569824b5ea',
        'client_secret': '44dafb59c4d94095a0a326022d7e82c1',
        'redirect_uri': 'http://wishtag.net/minsta/'
    }
else:
    CONFIG = {
        'client_id': '3dc77d748ec9434fba8d92569824b5ea',
        'client_secret': '44dafb59c4d94095a0a326022d7e82c1',
        'redirect_uri': 'http://127.0.0.1:8060/minsta/'
    }

session_opts = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True,
}
