import os
import sys
# coding=utf-8
#print 'Hello Hey yo'
#entrance of application

sys.path.append('/data/www/py/blog/blog')

#os.environ['PYTHON_EGG_CACHE'] = '/srv/www/ducklington.org/.python-egg'

def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
    ('Content-Length',
        str(len(output)))]
    start_response(status,response_headers)

    return [output]
import sys
import os
#sys.path.append(os.path.abspath(os.path.dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'  
#sys.path.append('/data/www/py/myapp')
import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
