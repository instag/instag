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
 
sys.path.append('/var/www/instag')
sys.path.append('/var/www/instag/src')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instag.settings.production")
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'instag.settings.production'
  
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()



    
    
    