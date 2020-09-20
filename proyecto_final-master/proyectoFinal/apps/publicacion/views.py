from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .forms import *
from .models import Publicaciones, Imagenes_Publicaciones
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.utils.funciones import PermisosMixin
from apps.usuarios.models import Usuario





def Publicacion(request, pk):

	context = {

	'publicacion': Publicaciones.objects.get(publicacion_id= pk),

	}
	
	return render(request,'publicacion/publi.html', context)


class Crear(LoginRequiredMixin,PermisosMixin,CreateView):
	rol = 'propietario'
	model = Publicaciones
	form_class = AltaPublicacion
	template_name = 'publicacion/crear.html'
	success_url = reverse_lazy('publicacion:crear')
	
	def form_valid(self, form):
		p = form.save()
		for m in self.request.FILES:
			Imagenes_Publicaciones.objects.create(publicaciones=p,img=m)

		return redirect(self.success_url)

	def current_user(self):
		current_user = self.request.user
		idd = current_user.id
		Publicaciones.objects.filter(usuario= idd)

		return redirect(self.success_url)


def Inicio(request):
	
	context = {

		'Publicacion': Publicacion.objects.all(),
		'form': Publicacion()

	}

	return render(request, 'publicacion/publi.html')


	


"""
class Editar(UpdateView):
	model = Publicaciones
	form_class = EditarPublicacion
	template_name = "publicacion/editar.html"
	success_url = reverse_lazy('home')
"""

class Borrar(DeleteView):
	model = Publicaciones
	success_url = reverse_lazy("propiedades.html")

class ListarPublicaciones(ListView):
	model = Publicaciones
	template_name = 'propiedades.html'

"""
class CargarImagenes(CreateView):
	model = Imagenes_Publicaciones
	form_class = AgregarImagenes
	template_name = 'publicacion/cargarImagenes.html'
	success_url = reverse_lazy('publicacion:crear')
"""
def ListarImagenes(request, fk):

	context = {


		'Imagenes': Imagenes_Publicaciones.objects.get(publicacion= fk),
	}

	return render(request, 'publicacion/publi.html', context)
