# In production set the environment variable like this:
#    DJANGO_SETTINGS_MODULE=instag.settings.production
from .base import *             # NOQA
import logging.config

# For security and performance reasons, DEBUG is turned off
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

# ALLOWED_HOSTS = [
#     'wishtag.net',
#     'www.wishtag.net',
# ]


# Must mention ALLOWED_HOSTS in production!
# ALLOWED_HOSTS = ["instag.com"]

# Cache the templates in memory for speed-up
loaders = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

TEMPLATES[0]['OPTIONS'].update({"loaders": loaders})
TEMPLATES[0].update({"APP_DIRS": False})

# Define STATIC_ROOT for the collectstatic command
STATIC_ROOT = join(BASE_DIR, '..', 'site', 'static')

# Log everything to the logs directory at the top
LOGFILE_ROOT = join(dirname(BASE_DIR), 'logs')

# Reset logging
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'proj_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': join(LOGFILE_ROOT, 'project.log'),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'project': {
            'handlers': ['proj_log_file'],
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['proj_log_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
    }
}

logging.config.dictConfig(LOGGING)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'instag_db',
        'USER': 'instag',
        'PASSWORD': 'instagpw',
        'HOST': 'ec2-52-68-85-32.ap-northeast-1.compute.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
                    "init_command": "SET storage_engine=MyISAM",
#                     'autocommit': True,
                    }        
    },
    'read': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'instag_db',
        'USER': 'instag',
        'PASSWORD': 'instagpw',
        'HOST': 'ec2-52-68-85-32.ap-northeast-1.compute.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
                    'init_command': 'SET storage_engine=MyISAM',
#                     'autocommit': True,
                    }
    },
}

