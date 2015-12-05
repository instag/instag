# -*- coding: utf-8 -*-
import os
from .hostname import HOSTNAME

print 555
if HOSTNAME.startswith('kin-no-macbook-pro.local'):
    print 111
    from .development import *
elif HOSTNAME.startswith('ip-172-31-22-249'): #本番
    print 222
    from .production import *
elif HOSTNAME.startswith('followkr01.cafe24.com'): #本番
    print 333
    from .production import *
