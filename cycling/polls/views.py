
from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from .models import Usuario
from django import forms

class Formulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField() #recibi valores aqui????
    edad = forms.CharField()
    mail = forms.CharField()
    nickname = forms.CharField()

def registro(request):
    if request.method == 'POST':#si el formulario es enviado
        form = Formulario(request.POST)

        if form.is_valid():#si es valido se procesan los datos
            
            return HttpResponseRedirect('gracias')
    else:
        form = Formulario()

    return render(request, 'index.html' , {
        'form' : form,
        })

def gracias(request):
    html='<html><body>"Gracias por registrarse...</body><html>'
    return HttpResponse(html)




def index(request):
    usuarios_por_nombre = Usuario.objects.order_by('-nombre')[:5]
    template = loader.get_template('polls/index.html')
    context = {        
    }
    return HttpResponse(template.render(context, request))

def listarusu(request):
    usuarios_por_nombre = Usuario.objects.order_by('-nombre')[:5]
    template = loader.get_template('polls/listarusu.html')
    context = {  'usuarios_por_nombre' : usuarios_por_nombre      
    }
    return render(request, 'polls/listarusu.html', context)
