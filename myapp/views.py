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



def info(request, topic, subtopic, subsubtopic):  #  subtopic='defaut' ne marche pas
    if subtopic is None: subtopic="nil"
    if subsubtopic is None: subsubtopic="nil"
    page=Page.objects.filter(definition=topic,  subtopic=subtopic, subsubtopic=subsubtopic) # 1 seule page normalement ; definition=topic
    documentPages=DocumentPage.objects.filter(page=page)                                     #  des docs lies ?
    document=Document.objects.filter(id=documentPages)
    #return HttpResponse(document)
    
    return render_to_response('info.html',                              # website/templates/information/info.html
                             {"page" : page, "document": document},
                             context_instance=RequestContext(request))


def merci(request) :
    output="<p>Merci !</p>"
    return HttpResponse(output)

#def edit(request) :
#   output="<p>Edition ici</p>"          
#   return HttpResponse(output)




