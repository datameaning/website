# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template

from mysite.myapp.models import *

import django.forms as forms
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

def index(request) :
    template=get_template('main_page.html')
    variables=Context({'page_body' : 'Hello this is our first page !'})
    output=template.render(variables)
    return HttpResponse(output)

def merci(request) :
    output="<p>Merci !</p>"
    return HttpResponse(output)

#def edit(request) :
#   output="<p>Edition ici</p>"          
#   return HttpResponse(output)


class EditeurModelForm(forms.ModelForm):

    class Meta:
        model = Editeur
        fields = ('nomEditeur','prenomEditeur')


def edit(request, editeur_id=None):

    if editeur_id is not None:
        editeur_id=int(editeur_id)
        editeur= get_object_or_404(Editeur, id=editeur_id)
    else:
        editeur = None


    if request.method == "POST":
        form = EditeurModelForm(data=request.POST, instance=editeur)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/merci/")
        else:
            form = EditeurModelForm(instance=editeur)

    else :
        form = EditeurModelForm(None, instance=editeur)


    return render_to_response("editeur_form.html", {'form' : form })


