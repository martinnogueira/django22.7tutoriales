from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

#import requests
#/home/martin/proyectopython/cyclingproject/cycling/polls/Logica/intprueba
#from polls.models import Usuario

#req = requests.post('http://127.0.0.1:8000/polls/registrar')
#print(req.POST['nombre'])


def registrar(request):
	print (request.POST['nombre'])