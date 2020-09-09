from django.shortcuts import render
from django.views.generic import CreateView, DeleteView 
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .forms import *
from .models import Publicaciones, Imagenes_Publicaciones
from django.urls import reverse_lazy
from django.forms import formset_factory


def Publicacion(request):	
	return render(request,'publicacion/publi.html')

def CargarImagenes(request):
	return render(request, 'publicacion/publi.html')

class Crear(CreateView):
	model = Publicaciones
	form_class = AltaPublicacion
	template_name = 'publicacion/crear.html'
	success_url = reverse_lazy('home')

class Editar(UpdateView):
	model = Publicaciones
	form_class = EditarPublicacion
	template_name = "publicacion/editar.html"
	success_url = reverse_lazy('home')


class Borrar(DeleteView):
	model = Publicaciones
	success_url = reverse_lazy("propiedades.html")

class ListarPublicaciones(ListView):
	model = Publicaciones
	template_name = 'propiedades.html'
