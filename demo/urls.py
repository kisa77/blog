from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^(?P<get_id>[\d]*)$', 'demo.views.home', name='home'),
    # url(r'^coupon/add$', 'demo.apps.blog.views.add_coupon', name='add_coupon'),
    # url(r'^demo/', include('demo.foo.urls')),
    url(r'^index.html', 'index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
