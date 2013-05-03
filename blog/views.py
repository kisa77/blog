#/usr/bin/python

import django
import sys
import os
import datetime
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
#import MySQLdb

#print sys.path

sys.path.append('/Users/Nemok/Documents/test')

#    import package
def home(self, get_id):

    dt = datetime.datetime.now()
    '''
    test=MySQLdb.connect(db='nemolee',host='myhost',user='u',passwd='p')
    cur = test.cursor()
    cur.execute('show databases;')
    for data in cur.fetchall():
            print data
    '''
    print os.path.abspath(os.path.dirname(__file__))
    return render_to_response('temp1.html', {'now_time':get_id})
#    print dir(package)


