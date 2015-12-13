#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import os
# import sys
# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instag.settings")
#     from django.core.management import execute_from_command_line
#     execute_from_command_line(sys.argv)
import os
import sys
import site

envpath = '/var/www/instag/instag/lib/python2.6/site-packages'

# we add currently directory to path and change to it
pwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(pwd)
sys.path = [pwd] + sys.path

print __file__
print pwd
# Append paths
site.addsitedir(envpath)

from hostname import HOSTNAME
if __name__ == "__main__":
    if HOSTNAME.startswith('followkr01.cafe24.com'): #本番
        print "本番 cafe24"
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instag.settings.production")
    elif HOSTNAME.startswith('wishtag.net'): #本番
        print "本番 ec2"
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instag.settings.production")
    else:
        print "local"
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instag.settings.development")
    
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fairy.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
