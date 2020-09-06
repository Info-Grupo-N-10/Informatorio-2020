from django.contrib import admin
from django.urls import path
from . import views

app_name="publicacion"

urlpatterns = [

	path('Publicacion/', views.Publicacion, name = 'publicacion'),
	path('Crear/', views.Crear.as_view(), name="crear"),
	path('Borrar/', views.Borrar.as_view(), name="borrar"),
	path('Editar/<str:pk>/', views.Editar.as_view(), name="editar"),

]