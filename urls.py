from django.conf.urls.defaults import *




mediaPrefix='/home/froloe/website/public/site_media'

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': mediaPrefix, 'show_indexes': True}),
    # href="/site_media/css/style.css"
    (r'^website/' , include('website.myapp.urls') ),
    # Uncomment the next line to enable the admin:
    #(r'^admin/(.*)', admin.site.root),  ALWAYSDATA
     (r'^admin/', include(admin.site.urls)), # Back Office part


     
)
