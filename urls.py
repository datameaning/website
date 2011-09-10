from django.conf.urls.defaults import *
from myapp.views import *
import botany.views


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
#    (r'^$',main_page),
 #   (r'^edit$',edit),
  #  (r'^edit/(?P<editeur_id>)\d+$',edit),
   # (r'^merci/$',merci),
    #(r'^botany/$',botany.views.botany_main_page),
   # (r'^botany/login/$','django.contrib.auth.views.login', {'template_name': 'botany/login.html'}),
   # (r'^botany/logout/$',botany.views.botany_logout_page),
   # (r'^botany/frtripleCreate/$',botany.views.botany_frtripleCreate_page),
#    (r'^botany/thanks/$',botany.views.botany_thanks_page),


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^website/' , include('mysite.myapp.urls') ),
    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),

     
)
