from django.shortcuts import render
from django.views.generic import CreateView, DeleteView 
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .forms import *
from .models import Publicacion
from django.urls import reverse_lazy


def Publicacion(request):	
	return render(request,'publicacion/publicacion.html')

class Crear(CreateView):
	model = Publicacion 
	form_class = AltaPublicacion
	template_name = 'publicacion/crear.html'
	success_url = reverse_lazy('home')

class Editar(UpdateView):
	model = Publicacion
	form_class = EditarPublicacion
	template_name = "publicacion/editar.html"
	success_url = reverse_lazy('home')


class Borrar(DeleteView):
	model = Publicacion
	success_url = reverse_lazy("propiedades.html")

class ListarPoductos(ListView):
	model = Publicacion
	template_name = 'propiedades.html'