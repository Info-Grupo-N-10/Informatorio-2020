from .models import Perfil
from django import forms


class AltaPerfil(forms.ModelForm):

	class Meta:
		model = Perfil
		fields = '__all__'


class EditarPerfil(forms.ModelForm):
 	class Meta:         
 		model = Perfil         
 		fields =  ["nombre", "telefono", "email", "descripcion", "imagen"]   
          


