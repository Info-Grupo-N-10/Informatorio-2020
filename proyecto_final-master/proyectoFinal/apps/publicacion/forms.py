from .models import Publicacion
from django import forms


class AltaPublicacion(forms.ModelForm):

	class Meta:
		model = Publicacion
		fields = '__all__'


class EditarPublicacion(forms.ModelForm):
 	class Meta:         
 		model = Publicacion         
 		fields =  ["precio", "descripcion", "ubicacion", "ambientes", "habitaciones", "baños", "cochera", "patio", "mascotas", "niños", "superficie", "servicios", "tipo_inmueble"]   
          


