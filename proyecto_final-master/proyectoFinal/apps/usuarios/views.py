from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
#from .forms import RegistroUsuario
from .models import Usuario

# class Registro(CreateView):
# 	model = Usuario
# 	form_class = RegistroUsuario
# 	template_name = 'usuarios/registro.html'
# 	success_url = reverse_lazy('home')

