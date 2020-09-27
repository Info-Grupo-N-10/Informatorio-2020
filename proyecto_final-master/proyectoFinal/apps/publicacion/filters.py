#Django Imports
from django.db import models
from django.shortcuts import render
from django import forms
from django.forms import widgets

#Libraries Imports
import django_filters
from django_filters import RangeFilter, ModelChoiceFilter, ModelMultipleChoiceFilter, BooleanFilter
from django_filters.widgets import BooleanWidget

#Repo Imports
from .models import *



class FiltroPublicacion (django_filters.FilterSet):
    
    servicios = django_filters.ModelMultipleChoiceFilter(queryset = Servicios.objects.all(),
                                                         widget = forms.CheckboxSelectMultiple )
    tipo_inmueble = django_filters.ModelChoiceFilter(queryset = Tipo_Inmueble.objects.all(),
                                                      widget = forms.Select, required = False )
    ubicacion = django_filters.ModelChoiceFilter(queryset = Zona.objects.all(), widget = forms.Select,
                                                 required = False)
    mascotas = django_filters.BooleanFilter(field_name="mascotas", widget = forms.CheckboxInput, required = False)
    patio = django_filters.BooleanFilter(field_name="patio", widget = forms.CheckboxInput, required = False)
    cochera = django_filters.BooleanFilter(field_name="cochera", widget = forms.CheckboxInput, required = False)
    niños = django_filters.BooleanFilter(field_name="niños", widget = forms.CheckboxInput, required = False)
    
    # puntuacion = django_filters.NumberFilter(field_name="ACA VA EL CAMPO PUNTUACIONES DE PUBLICACIONES",
    #                                          lookup_expr="gte")
    
    class Meta:
        model = Publicaciones
        fields = {
            "precio": ["lte",],
            "habitaciones": ["gte",],
            "ambientes": ["gte",],
            "baños": ["gte",],
            "superficie": ["gte",],
        }
       
        
        
