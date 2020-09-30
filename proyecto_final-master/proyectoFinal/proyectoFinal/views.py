from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse_lazy

from apps.favoritos.models import Favoritos
from apps.publicacion.models import Publicaciones
from django.views.generic.list import ListView

# class Home(ListView):
#     model = Publicaciones
#     template_name = 'home.html'

#     def get_context_data(self, **kwargs):
#         context = super(Home, self).get_context_data(**kwargs)
#         context['publicaciones'] = Publicaciones.objects.all().order_by('-publicacion_id')
#         return context

def Home(request):
    p = Publicaciones.objects.all()
    f = Favoritos.objects.all()

    context = {
    'publis': p,
    'favs': f, }

    return render(request, 'home.html', context)

def Registro(request):
	return render(request, 'registro.html') #home

def Usuarios(request):
	return render(request, 'usuarios.html')#propiedades

class LogoutView(View):
	success_url = reverse_lazy('home')

#Registro, Perfil, Usuarios, Propiedades, Publicación, Favoritos