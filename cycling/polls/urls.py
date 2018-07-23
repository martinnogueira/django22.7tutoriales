from django.urls import path



from django.conf import settings
from django.conf.urls.static import static


from . import views

app_name = 'polls'
# lista con nuevas vistas 
urlpatterns = [
    path('registrar', views.index, name='index'),
    #pa mostrar un usuario de la base creo
    path('listar', views.listarusu, name='listarusu'),

    path('registro', views.registro,name='registro'),
    path('gracias', views.gracias,name='gracias'),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
