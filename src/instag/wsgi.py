# -*- coding: utf-8 -*-
"""
WSGI config for instag project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""



# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instag.settings.production")
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()



import os

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instag.settings.production")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings_dev")

from django.core.wsgi import get_wsgi_application

from dj_static import Cling
application = Cling(get_wsgi_application())






# import site
# site.addsitedir('/var/www/instag/instag/lib/python2.7/site-packages')
# import os
# import sys
#  
# sys.path.append('/var/www/instag')
# sys.path.append('/var/www/instag/src')
# # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instag.settings.production")
#  
# os.environ['DJANGO_SETTINGS_MODULE'] = 'instag.settings.production'
#   
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()



    
    
    