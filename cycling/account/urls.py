from django.conf.urls import url
from . import views
from django.contrib.auth.views import login , logout , password_reset , password_reset_done, password_reset_confirm,password_reset_complete

urlpatterns = [
    url(r'^$',views.home),
    url(r'^login/$', login, {'template_name': 'account/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'account/logout.html'}),
    url(r'^registrar/$',views.registrar,name='registrar'),
    url(r'^perfil/$', views.perfil , name='perfil'),
    url(r'^perfil/editarperfil$', views.editarperfil , name='editarperfil'),
	url(r'^cambiar_password/$', views.cambiar_password , name='cambiar_password'),
	url(r'^reset-password/$', password_reset,name='reset_password'),
	url(r'^reset-password/done/$',password_reset_done,name='password_reset_done'),
	url(r'^reset-password/confirm(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm,name='password_reset_confirm'),
	url(r'^reset-password/complete/$',password_reset_complete,name='password_reset_complete'),

]
