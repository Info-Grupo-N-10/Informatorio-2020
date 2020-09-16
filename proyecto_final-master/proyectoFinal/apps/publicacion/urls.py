from django.contrib import admin
from django.urls import path
from . import views


app_name="publicacion"

urlpatterns = [

	path('Propiedad/', views.Publicacion, name = 'publi'),
	#path('CargarImagen/', views.CargarImagenes.as_view(), name='imagenes'),
	path('Listar/', views.ListarPublicaciones.as_view(), name='listar'),
	path('Crear/', views.Crear.as_view(), name="crear"),
	path('Borrar/', views.Borrar.as_view(), name="borrar"),
	path('Editar/<str:pk>/', views.Editar.as_view(), name="editar"),
	path('ListarImagenes/', views.ListarImagenes, name='listarImg'),

	]