from django.contrib import admin
from django.urls import path
from . import views

app_name="perfil"

urlpatterns = [

	path('Perfil/', views.Perfil, name = 'perfil'),

]