# -*- coding: utf-8 -*-
"""
WSGI config for instag project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.production")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


# import site
# site.addsitedir('/home/ec2-user/.virtualenvs/instag/lib/python2.7/site-packages')
# import os
# import sys
# 
# sys.path.append('/var/www/instag')
# sys.path.append('/var/www/instag/src')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apple.settings")
# 
# os.environ['DJANGO_SETTINGS_MODULE'] = 'instag.settings'
#  
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
# from django.conf import settings
# if settings.DEBUG:
#     try:
#         import django.views.debug
#         import six
#         from werkzeug.debug import DebuggedApplication
#  
#         def null_technical_500_response(request, exc_type, exc_value, tb):
#             six.reraise(exc_type, exc_value, tb)
#  
#         django.views.debug.technical_500_response = null_technical_500_response
#         application = DebuggedApplication(application, evalex=True)
#     except ImportError:
#         pass
    
    