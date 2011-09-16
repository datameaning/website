# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template

from website.myapp.models import *

import django.forms as forms
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

def index(request) :
    template=get_template('datameaning.htm')
    variables=Context({'page_body' : 'Hello this is our first page !'})
    output=template.render(variables)
    return HttpResponse(output)

def merci(request) :
    output="<p>Merci !</p>"
    return HttpResponse(output)

#def edit(request) :
#   output="<p>Edition ici</p>"          
#   return HttpResponse(output)




