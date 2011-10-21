from django.conf.urls.defaults import *
from django.http import HttpResponseRedirect

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'website.myapp.views.index'),
        (r'^(?P<topic>\w+)/$', 'website.myapp.views.info'),
       # (r'^ajax/$', 'website.myapp.views.ajax'),	
   )
