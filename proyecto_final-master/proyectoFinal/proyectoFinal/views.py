from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse_lazy

def Home(request):
	return render(request, 'home.html')#home

def Registro(request):
	return render(request, 'registro.html') #home

def Usuarios(request):
	return render(request, 'usuarios.html')#propiedades

class LogoutView(View):
	success_url = reverse_lazy('home')

#Registro, Perfil, Usuarios, Propiedades, Publicación, Favoritos