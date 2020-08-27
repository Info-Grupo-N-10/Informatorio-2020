
from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),

     path('', views.Home , name = 'home'),
     path('Regigastrarse', views.Registro, name = 'registro'),
     path('Usuarios', views.Usuarios, name = 'usuarios'), 
     path('Propiedades', views.Propiedades, name = 'propiedades'),#app catalogo de publicaciones
     

     #urls otras app
	 path('perfil', include('apps.perfil.urls')),
	 path('publicacion', include('apps.publicacion.urls')),
	 path('favoritos', include('apps.favoritos.urls')),

]
