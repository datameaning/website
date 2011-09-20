# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template

from website.myapp.models import *  #  import Page, DocumentPage, Document, UserExt, SiteLanguage


import django.forms as forms
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

def index(request) :
    mainColumnSections 	= 	Page.objects.filter(definition='edito')
##   main_column_picture_id	=	DocumentPage.objects.filter(page=main_column)
##   main_column_picture		=	Document.objects.filter(id=main_column_picture_id)
##   right_column 	= 	Page.objects.filter(definition='aside')
##   right_column_picture_id	=	DocumentPage.objects.filter(page=right_column)
##   right_column_picture		=	Document.objects.filter(id=main_column_picture_id)

    return render_to_response('index.htm',
                             {"mainColumnSections" : mainColumnSections},
                             context_instance=RequestContext(request))


def info(request, url):                                #  (r'^(demos)/$', 'website.myapp.views.info'),	url = demo 
	info = Page.objects.filter(definition=url)
	picturePage	=	DocumentPage.objects.filter(page=info)
	picture		=	Document.objects.filter(id=picturePage)
	return render_to_response('wsite/information/info_fr.html', 
								{'info': info, 'picture': picture}, 
								context_instance=RequestContext(request))

def merci(request) :
    output="<p>Merci !</p>"
    return HttpResponse(output)

#def edit(request) :
#   output="<p>Edition ici</p>"          
#   return HttpResponse(output)




