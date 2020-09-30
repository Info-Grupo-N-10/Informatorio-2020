from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse_lazy

from apps.usuarios.models import Usuario
from apps.publicacion.models import Publicaciones
from django.views.generic.list import ListView

import random

def Home(request):
    u = list(Usuario.objects.all())
    p = Publicaciones.objects.all()
    r = random.sample(u, 3)

    context = {
    'publis': p,
    'usuarios': r, }

    return render(request, 'home.html', context)

    return render(request, 'home.html', context)

def Registro(request):
	return render(request, 'registro.html') #home

def Usuarios(request):
	return render(request, 'usuarios.html')#propiedades

class LogoutView(View):
	success_url = reverse_lazy('home')

#Registro, Perfil, Usuarios, Propiedades, Publicación, Favoritos