from django.db import models
from django.shortcuts import render
import django_filters
from django import forms
from django.db import models
from django.forms import widgets

#Repo Imports
from .models import *

# Create your views here.

# class RangeWidget(SuffixedMultiWidget):
#     suffixes = ['min', 'max']

class FiltroPublicacion (django_filters.FilterSet):



    class Meta:

        model = Publicaciones
        fields = {
            'publicacion_id': ['exact',],
            'habitaciones': ['gte',],
            'baños': ['gte',],
            'cochera': ['exact',],
            'patio': ['exact',],
            'mascotas': ['exact',],
            'niños': ['exact',],
            'superficie': ['gte',],
            'ubicacion': ['__ubicacion'],          
            }
        
            
            
        

# class FiltroServicios(django_filters.FilterSet):
   
#    class Meta:

#        model = Servicios
#        fields = '__all__'

# class FiltrosZona(django_filters.FilterSet):

#     class Meta:

#         model = Zona
#         fields = '__all__'

# class FiltrosTipoInmueble(django_filters.FilterSet):
     
#      class Meta:
#          model = Tipo_Inmueble
#          fields = '__all__'