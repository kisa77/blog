from django.conf.urls import patterns, include, url
from blog.views import Views
import os
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import django
import sys
import os
import datetime
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect, QueryDict
from django.conf.urls.defaults import *
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import html
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
# admin.autodiscover()


def home(request):

    #dt = datetime.datetime.now()
    '''
    test=MySQLdb.connect(db='nemolee',host='myhost',user='u',passwd='p')
    cur = test.cursor()
    cur.execute('show databases;')
    for data in cur.fetchall():
            print data
    '''
#    print os.path.abspath(os.path.dirname(__file__))
    return render_to_response('temp1.html', {'now_time':'id'})
#    print dir(package)

instance = Views;

urlpatterns = patterns('',
    # Examples:
    # url(r'^(?P<get_id>[\d]*)$', 'demo.views.home', name='home'),
    # url(r'^coupon/add$', 'demo.apps.blog.views.add_coupon', name='add_coupon'),
    # url(r'^demo/', include('demo.foo.urls')),
    url(r'^$', home),
    url(r'^index', home),
    url(r'^about', instance.home),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('blog.apps.blog.views',
    url(r'^post/(?P<post_id>\w*)$', 'post', name='post_id'),
)
