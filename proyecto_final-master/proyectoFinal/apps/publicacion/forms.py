from .models import *
from django import forms
from django.db import transaction
from .admin import *



class AltaPublicacion(forms.ModelForm):
	servicios = forms.ModelMultipleChoiceField(queryset=Servicios.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)
	
	
	class Meta:
		model = Publicaciones
		fields = '__all__'
		


class EditarPublicacion(forms.ModelForm):
	class Meta:         
		model = Publicaciones        
		fields =  ["precio", "descripcion", "ubicacion", "ambientes", "habitaciones", "baños", "cochera", "patio", "mascotas","niños", "superficie", "servicios", "tipo_inmueble"]   


class AgregarImagenes(forms.ModelForm):
	class Meta:
		model = Imagenes_Publicaciones
		fields = "__all__"         