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

sys.path.append('/var/www/instag')
sys.path.append('/var/www/instag/src')

from hostname import HOSTNAME
if __name__ == "__main__":
    if HOSTNAME.startswith('followkr01.cafe24.com'): #本番
        print "本番"
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instag.settings.production")
    else:
        print "local"
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instag.settings.development")
    
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fairy.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
