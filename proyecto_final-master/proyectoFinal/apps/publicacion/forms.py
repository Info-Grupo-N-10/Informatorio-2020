from .models import *
from django import forms
from django.db import transaction
from .admin import *
from apps.usuarios.models import Usuario
from .models import Publicaciones





class AltaPublicacion(forms.ModelForm):
	servicios = forms.ModelMultipleChoiceField(queryset=Servicios.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)
	#usuario = forms.ModelMultipleChoiceField(queryset=Publicaciones.objects.filter(usuario= Usuario.pk))

	
	class Meta:
		model = Publicaciones
		fields = '__all__'
		exclude = ['usuario']
	
	
	
	 # def __init__(self, *args, **kwargs):
	 # 	self.fields['usuario'].initial = kwargs['instance'].UsuarioPublicacion.id


		

class EditarPublicacion(forms.ModelForm):
	class Meta:         
		model = Publicaciones        
		fields =  ["precio", "descripcion", "ubicacion", "ambientes", "habitaciones", "baños", "cochera", "patio", "mascotas","niños", "superficie", "servicios", "tipo_inmueble"]   



# 

class AgregarImagenes(forms.ModelForm):
	class Meta:
		model = Imagenes_Publicaciones
		fields = "__all__"         



	

