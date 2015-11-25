# -*- coding: utf-8 -*-
import os
from .hostname import HOSTNAME

if HOSTNAME.startswith('kin-no-macbook-pro.local'):
    from .development import *
elif HOSTNAME.startswith('followkr01.cafe24.com'): #本番
    from .production import *
