#/usr/bin/python

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
from django.db.models import Q
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms.util import ErrorList
from django.utils import html
from django.core import urlresolvers
#import MySQLdb

#print sys.path

#sys.path.append('/Users/Nemok/Documents/test')

#    import package
class Views():
    def home(request):

        dt = datetime.datetime.now()
        '''
        test=MySQLdb.connect(db='nemolee',host='myhost',user='u',passwd='p')
        cur = test.cursor()
        cur.execute('show databases;')
        for data in cur.fetchall():
                print data
        '''
        #print os.path.abspath(os.path.dirname(__file__))
        return render_to_response('temp1.html', {'now_time':'get_id'})
    #    print dir(package)

        print "fuck you"
    def index(request):
        print "fuck you"
        print "hello there"

    def about_me(request):
        print 'Hey there'
