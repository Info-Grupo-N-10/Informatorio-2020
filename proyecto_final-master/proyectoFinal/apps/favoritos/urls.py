from django.contrib import admin
from django.urls import path
from . import views

app_name="favoritos"

urlpatterns = [

	 path('Favoritos/', views.lista_de_favoritos, name = 'favoritos'),
	 path('marcar/favorito/<int:pk>/marcador', views.Marcador, name = 'marcar'),

]