from django.contrib import admin
from django.urls import path
from . import views

app_name="perfil"

urlpatterns = [

	path('Perfil/', views.Perfil, name = 'perfil'),
	path('agente1/', views.Agente1, name = "agente1"),
	path('agente2/', views.Agente2, name = "agente2"),
	path('agente3/', views.Agente3, name = "agente3"),
]