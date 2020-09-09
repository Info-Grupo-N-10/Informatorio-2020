from .models import Publicaciones, Imagenes_Publicaciones
from django import forms



class AltaPublicacion(forms.ModelForm):

	class Meta:
		model = Publicaciones
		fields = '__all__'
"""
class ImagenesForm(forms.ModelForm):
    image = forms.ImageField(label = "Image")
	class Meta:
    	model = Imagenes_Publicaciones
		fields = 'image'
"""

class EditarPublicacion(forms.ModelForm):
 	class Meta:         
 		model = Publicaciones        
 		fields =  ["precio", "descripcion", "ubicacion", "ambientes", "habitaciones", "baños", "cochera", "patio", "mascotas","niños", "superficie", "servicios", "tipo_inmueble"]   
          

