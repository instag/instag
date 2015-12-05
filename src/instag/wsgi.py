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




import site
site.addsitedir('/home/ec2-user/.virtualenvs/instag/lib/python2.7/site-packages')

import os
import sys

# sys.path.append('/home/ec2-user/.virtualenvs/instag/lib/python2.7/site-packages')
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
# site.addsitedir("/home/ec2-user/.virtualenvs/instag/lib/python2.7/site-packages")



print os.path.dirname(__file__)
# /var/www/instag/src/instag
 
paths = (
   os.path.abspath(os.path.join(os.path.dirname(__file__), '../instag')),
   os.path.abspath(os.path.join(os.path.dirname(__file__), '../')),
   )

for path in paths:
   sys.path.insert(0,path)


os.environ['DJANGO_SETTINGS_MODULE'] = 'instag.settings.production'

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instag.settings.production")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


# Wrap werkzeug debugger if DEBUG is on
from django.conf import settings
if settings.DEBUG:
    try:
        import django.views.debug
        import six
        from werkzeug.debug import DebuggedApplication

        def null_technical_500_response(request, exc_type, exc_value, tb):
            six.reraise(exc_type, exc_value, tb)

        django.views.debug.technical_500_response = null_technical_500_response
        application = DebuggedApplication(application, evalex=True)
    except ImportError:
        pass
