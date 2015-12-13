# -*- coding: utf-8 -*-
import os
from .hostname import HOSTNAME

if HOSTNAME.startswith('kin-no-macbook-pro.local'):
    from .development import *
elif HOSTNAME.startswith('ip-172-31-22-249'): #本番
    from .production import *
elif HOSTNAME.startswith('wishtag.net'): #本番
    from .production import *
elif HOSTNAME.startswith('followkr01.cafe24.com'): #本番
    from .production import *
