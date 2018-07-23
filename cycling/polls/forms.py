from django import forms

class Formulario(forms.Form):
	nombre = forms.CharField()
	apellido= forms.CharField()
	edad= forms.CharField()
	mail= forms.CharField()
	nickname= forms.CharField()