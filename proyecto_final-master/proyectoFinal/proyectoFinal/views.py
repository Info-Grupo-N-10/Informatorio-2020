from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse_lazy

from apps.publicacion.models import Publicaciones
from django.views.generic.list import ListView

class Home(ListView):
    model = Publicaciones
    template_name = 'home.html'

# def Home(request):
# 	ultimas_propiedades = Publicaciones.objects.all().order_by("-precio")
# 	context = {"ultimas":ultimas_propiedades}

# 	return render(request, 'home.html', context)

def Registro(request):
	return render(request, 'registro.html') #home

def Usuarios(request):
	return render(request, 'usuarios.html')#propiedades

class LogoutView(View):
	success_url = reverse_lazy('home')

#Registro, Perfil, Usuarios, Propiedades, Publicación, Favoritos