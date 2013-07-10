import os
import sys
# coding=utf-8
#entrance of application

sys.path.append('/data/www/py/blog/blog')
sys.path.append('/data/www/py/blog')
os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
