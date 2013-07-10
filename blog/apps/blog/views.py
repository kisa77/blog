# Create your views here.
import os
import sys
import datetime
import random
from models import coupon
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

sys.path.append('/Users/Nemok/Documents/test')

def add_coupon(self):

    dt = datetime.datetime.now()
    for x in range(2):
        new_coupon = coupon(cTitle = 'dddd', cid = 110000)
        new_coupon.save()

    all_coupons = coupon.objects.all()
    '''
    test=MySQLdb.connect(db='nemolee',host='myhost',user='u',passwd='p')
    cur = test.cursor()
    cur.execute('show databases;')
    for data in cur.fetchall():
            print data
    '''
    return render_to_response('temp1.html', {
             'now_time':dt, 
             'show_coupon' : True,
             'all_coupons': all_coupons,
                })
def post(request, post_id):
    #postId = get_object_or_404(post_id, name=post_id)

    return render_to_response('post/post.html', {
        'post_id' : post_id
        })
