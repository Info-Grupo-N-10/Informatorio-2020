from .models import Publicaciones, Imagenes_Publicaciones, Servicios, Zona
from django import forms
from django.db import transaction





class AltaPublicacion(forms.ModelForm):
	servicios = forms.ModelMultipleChoiceField(queryset=Servicios.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)

	class Meta:
		model = Publicaciones
		fields = '__all__'


class EditarPublicacion(forms.ModelForm):
	servicios = forms.ModelMultipleChoiceField(queryset=Servicios.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)
	class Meta:
		model = Publicaciones
		fields = '__all__'
		exclude = ['publicacion_id'] 


	
		


