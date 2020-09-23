#Django Imports
from django.db import models
from django.shortcuts import render
import django_filters
from django import forms
from django.forms import widgets
from .models import *


#Repo Imports




# class RangeWidget(SuffixedMultiWidget):
#     suffixes = ['min', 'max']

class FiltroPublicacion (django_filters.FilterSet):
    
    precio__lte = django_filters.NumberFilter(name='precio', lookup_expr='lte')
    servicios = django_filters.ModelMultipleChoiceFilter(queryset=Servicios.objects.all(),
                                                         widget= forms.CheckboxSelectMultiple )
    tipo_inmueble = django_filters.ModelChoiceFilter(to_field_name='tipo_inmueble', queryset=Tipo_Inmueble.objects.all(),
                                                     widget = CheckboxSelect )
    
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
            'servicios': [],
            'tipo_inmueble': [],
        }