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
from apps.publicacion.filters import FiltroPublicacion


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
        p = form.save(commit=False)
        p.usuario = self.request.user
        p.save()
        for m in self.request.FILES:
            print(m)
            Imagenes_Publicaciones.objects.create(publicacion=p, img=m)

        return redirect(self.success_url)

class Editar(PermisosMixin, UpdateView):
    rol = 'propietario'
    model = Publicaciones
    form_class = EditarPublicacion
    template_name = "publicacion/editar.html"
    success_url = reverse_lazy('publicacion:public')


class Borrar(LoginRequiredMixin,PermisosMixin,DeleteView):
    rol = 'propietario'
    model = Publicaciones
    def borrar(request):
        u = request.user
        if publicacion.usuario == u.id:
            permiso = 'permitido'
    success_url = reverse_lazy('home')

class ListarPublicaciones(ListView):
    model = Publicaciones
    template_name = 'publicacion/propiedades.html'


def Inicio(request):

    context = {

        'Publicacion': Publicacion.objects.all(),
        'form': Publicacion()

    }

    return render(request, 'publicacion/publicacion.html')


def Filtros(request):
    
    publicaciones = FiltroPublicacion(request.GET, queryset=Publicaciones.objects.all().order_by("-precio"))
    context = { "inmuebles" : publicaciones }
    print(context)
    #precio_max = Publicaciones.objects.
    return render(request, "publicacion/filtrado.html", context)