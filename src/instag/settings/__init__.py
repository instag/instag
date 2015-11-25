# -*- coding: utf-8 -*-

import os
from .hostname import HOSTNAME

print HOSTNAME

if HOSTNAME.startswith('kin-no-macbook-pro.local'):
    print 11111
    from .development import *
elif HOSTNAME.startswith('followkr01.cafe24.com'): #本番
    print 233
    from .production import *
