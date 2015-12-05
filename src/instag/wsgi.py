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


# import site
# site.addsitedir('/home/ec2-user/.virtualenvs/instag/lib/python2.7/site-packages')
# import os
# import sys
# 
# paths = (
#    os.path.abspath(os.path.join(os.path.dirname(__file__), '../instag')),
#    os.path.abspath(os.path.join(os.path.dirname(__file__), '../')),
#    )
# 
# for path in paths:
#     print path
#     sys.path.insert(0,path)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'instag.settings.production'
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
    
    
    
import os
import sys
import site
site.addsitedir('/home/ec2-user/.virtualenvs/instag/lib/python2.7/site-packages')

path = '/var/www/instag'
if path not in sys.path:
    sys.path.append(path)

sys.stdout = sys.stderr
print sys.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'instag.settings.production'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()