from django.shortcuts import render
from django.views.generic import CreateView, DeleteView 
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .forms import *
from .models import Perfil
from django.urls import reverse_lazy


def Perfil_Usuarios(request):  
    return render(request,'perfil/perfil.html')

class Registro(CreateView):
    model = Perfil
    form_class = RegistroUsuario
    template_name = 'perfil/registro.html'
    success_url = reverse_lazy('home')

class Crear(CreateView):
    model = Perfil 
    form_class = RegistroUsuario
    template_name = 'perfil/editar.html'
    success_url = reverse_lazy('home')

# class Editar(UpdateView):
#     model = Usuario
#     form_class = RegistroUsuario
#     template_name = "perfil/editar.html"
#     success_url = reverse_lazy('home')


class Borrar(DeleteView):
    model = Perfil
    success_url = reverse_lazy("home")

class ListarPerfiles(ListView):
    model = Perfil
    template_name = 'perfil/todos.html'