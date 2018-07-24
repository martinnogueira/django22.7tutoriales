from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from account.forms import editarperfilform 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
#este import es para no dejar que entren a urls como /perfil sin estar loguqeados
from django.contrib.auth.decorators import login_required 


# Create your views here.
@login_required
def home(request):
	numbers = [1,2,3,4,5]
	name = 'martin nogueira'
	args = {'myname' : name , 'numbers':numbers}
	return render(request, 'account/home.html',args)



def registrar(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = UserCreationForm()

		args = {'form' : form }
		return render(request, 'account/reg_form.html' ,args)

@login_required #ESTO BLOQUEA VER PERFIL SI NO ESTAS LOGUEADO
def perfil(request):
	args = {'user' : request.user}
	return render (request, 'account/perfil.html',args)

@login_required
def editarperfil(request):
	if request.method == 'POST':
		form = editarperfilform(request.POST,instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/account/perfil')
	else:
		form = editarperfilform(instance=request.user)
		args = {'form': form}
		return render(request, 'account/editarperfil.html', args)

@login_required
def cambiar_password(request):
	if request.method =="POST":
		form = PasswordChangeForm(data=request.POST,user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return redirect('/account/perfil')
		else: 
			return redirect('/account/cambiar_password.html')
	else:
		form = PasswordChangeForm(user=request.user)

		args = { 'form' : form}
		return render(request,'account/cambiar_password.html',args)
