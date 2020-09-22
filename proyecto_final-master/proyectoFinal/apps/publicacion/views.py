from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .forms import *
from .models import Publicaciones, Imagenes_Publicaciones, Servicios
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.utils.funciones import PermisosMixin
from apps.usuarios.models import Usuario
from .filters import *
from django_filters.views import FilterView


def Publicacion(request, pk):

	context = {

	'publicacion': Publicaciones.objects.get(publicacion_id= pk),

	}

	return render(request,'publicacion/publicacion.html', context)


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

class Editar(UpdateView):
	 model = Publicaciones
	 form_class = EditarPublicacion
	 template_name = "publicacion/editar.html"
	 success_url = reverse_lazy('publicacion:public')


class Borrar(LoginRequiredMixin,PermisosMixin,DeleteView):
	rol = 'propietario'
	model = Publicaciones
	success_url = reverse_lazy('home')

# class ListarPublicaciones(ListView):
# 	model = Publicaciones
# 	template_name = 'publicacion/propiedades.html'

def ListarPublicaciones(request):
	#todos = Publicaciones.objects.all()
	filtro_publicacion = FiltroPublicacion(request.GET, queryset=Publicaciones.objects.all() )
	# filtro_servicios = FiltroServicios(request.GET, queryset=Servicios.objects.all())
	# filtro_inmubles = FiltrosTipoInmueble(request.GET, queryset=Tipo_Inmueble.objects.all())
	# filtro_zona = FiltrosZona(request.GET, queryset=Zona.objects.all())

	context = {
	'publicaciones': filtro_publicacion,
	}

	return render(request, 'publicacion/propiedades.html', context)
	
# template_name = 'publicacion/propiedades.html'
# filterset_class = FiltroPublicacion
# #model = Publicaciones 





# def Filters(request):

# 	filtro_publicacion = FiltroPublicacion(request.GET, queryset=Publicaciones.objects.all() )
# 	filtro_servicios = FiltroServicios(request.GET, queryset=Servicios.objects.all())
# 	filtro_inmubles = FiltrosTipoInmueble(request.GET, queryset=Tipo_Inmueble.objects.all())
# 	filtro_zona = FiltrosZona(request.GET, queryset=Zona.objects.all())

# 	context = {
# 	'publicaciones': filtro_publicacion,
# 	'servicios': filtro_servicios,
# 	'inmuebles': filtro_inmubles,
# 	'zona': filtro_zona }
# 	return render(request, 'publicacion/filtros.html', context)



