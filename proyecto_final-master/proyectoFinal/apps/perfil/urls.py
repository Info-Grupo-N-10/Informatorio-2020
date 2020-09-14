from django.contrib import admin
from django.urls import path
from . import views

app_name="perfil"

urlpatterns = [

    path('Perfil/', views.Perfil_Usuarios, name = 'perfil'),
    path('Crear/', views.Crear.as_view(), name="crear"),
    path('Borrar/<int:pk>/', views.Borrar.as_view(), name="borrar"),
    path('Editar/<int:pk>/', views.Editar.as_view(), name="editar"),
]