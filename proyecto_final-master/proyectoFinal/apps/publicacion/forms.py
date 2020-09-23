from .models import Publicaciones, Imagenes_Publicaciones, Servicios
from django import forms


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