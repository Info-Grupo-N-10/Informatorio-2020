from .models import Publicaciones, Imagenes_Publicaciones, Servicios, Tipo_Inmueble
from django import forms


class AltaPublicacion(forms.ModelForm):
	servicios = forms.ModelMultipleChoiceField(queryset=Servicios.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)
	tipo_inmueble = forms.ModelChoiceField(queryset=Tipo_Inmueble.objects.all(), widget=forms.Select(attrs={'class':'form-control'}),required=False)
	class Meta:
		model = Publicaciones
		fields = '__all__'


class EditarPublicacion(forms.ModelForm):
    servicios = forms.ModelMultipleChoiceField(queryset=Servicios.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)
    
    class Meta:
        model = Publicaciones
        fields = '__all__'
        exclude = ['publicacion_id']