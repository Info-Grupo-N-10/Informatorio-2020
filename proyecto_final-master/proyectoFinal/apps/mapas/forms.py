from .models import Ubicacion
from django import forms
from apps.publicacion.models import Publicaciones


class UbicacionForm(forms.ModelForm):
	lat = forms.CharField(label='Latitud', max_length=100)
	lng = forms.CharField(label='Longitud', max_length=100)

	class Meta:
		model = Ubicacion
		fields = ['lat', 'lng']
