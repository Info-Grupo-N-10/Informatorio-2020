from django.contrib import admin
from django.urls import path
from . import views

app_name="publicacion"

urlpatterns = [

	path('Publicacion/', views.Publicacion, name = 'publicacion'),

]