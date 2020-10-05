from django.shortcuts import render, redirect, reverse
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
from apps.mapas.models import Ubicacion
from django.http import HttpResponse, HttpResponseRedirect


def Publicacion(request, pk):
    p = Publicaciones.objects.get(publicacion_id= pk)
    r = Reseña.objects.filter(post=p).order_by('id')
    m = Ubicacion.objects.get(publicacion=pk)

    if request.method == 'POST':
        reseña_form = Reseñas(request.POST or None)
        if reseña_form.is_valid():
            mensaje = request.POST.get('mensaje')
            r = Reseña.objects.create(post=p, usuario=request.user, mensaje=mensaje)
            r.save()
            return HttpResponseRedirect(reverse('publicacion:public', args=[(pk)]))
    else:
        reseña_form = Reseñas()



    context = { 
                'publicacion': p, 
                'reseña_form': reseña_form,
                'lat': m.lat,
                'lng': m.lng, 
    }


    return render(request,'publicacion/publicacion.html', context)


class Crear(LoginRequiredMixin,PermisosMixin,CreateView):
    rol = 'propietario'
    model = Publicaciones
    form_class = AltaPublicacion
    template_name = 'publicacion/crear.html'
    success_url = reverse_lazy('publicacion:propiedades')

    def form_valid(self, form):
        p = form.save(commit=False)
        p.usuario = self.request.user
        p.save()

        for i in form.cleaned_data['servicios']:
            x = Servicios.objects.get(nombre=i)
            p.servicios.add(x)

        for m, j in self.request.FILES.items():
            Imagenes_Publicaciones.objects.create(publicacion=p, img=j)

        return redirect(self.success_url)

class Editar(PermisosMixin, UpdateView):
    rol = 'propietario'
    model = Publicaciones
    form_class = EditarPublicacion
    template_name = "publicacion/editar.html"

    def get_success_url(self):
        return reverse_lazy('publicacion:public',kwargs={'pk':self.kwargs['pk'] })



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

def Filtros(request):
    context = {}
    orden = request.GET.get("orden", None)
        
    if orden:
        if orden == "1":
            publicaciones = FiltroPublicacion(request.GET, queryset=Publicaciones.objects.all().
                                              order_by("precio"))
        elif orden == "2":
            publicaciones = FiltroPublicacion(request.GET, queryset=Publicaciones.objects.all().
                                              order_by("-precio"))
    else:
        publicaciones = FiltroPublicacion(request.GET, queryset=Publicaciones.objects.all())      
    
    context["publicaciones"] = publicaciones.qs
    context["formulario"] = publicaciones.form
    
    return render(request, "publicacion/filtrado.html", context)


class borrarReseña(DeleteView):
    model = Reseña
    success_url = reverse_lazy('publicacion:propiedades')