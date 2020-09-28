from .models import Publicaciones, Imagenes_Publicaciones, Servicios, Tipo_Inmueble, Zona
from django import forms


class AltaPublicacion(forms.ModelForm):
    servicios = forms.ModelMultipleChoiceField(queryset=Servicios.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)
    tipo_inmueble = forms.ModelChoiceField(queryset=Tipo_Inmueble.objects.all(), widget=forms.Select(attrs={'class':'form-control'}),required=False)
    ubicacion = forms.ModelChoiceField(queryset=Zona.objects.all(), widget=forms.Select(attrs={'class':'form-control'}), required=False)


    class Meta:
        model = Publicaciones
        fields = '__all__'
        exclude = ['publicacion_id', 'usuario']

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].widget = forms.TextInput(attrs={'class':'input--style-6'})
        self.fields['precio'].widget = forms.NumberInput(attrs={'class':'input--style-6'})
        self.fields['descripcion'].widget = forms.Textarea(attrs={'class':'textarea--style-6'})
        self.fields['ambientes'].widget = forms.NumberInput(attrs={'class':'input--style-6'})
        self.fields['habitaciones'].widget = forms.NumberInput(attrs={'class':'input--style-6'})
        self.fields['baños'].widget = forms.NumberInput(attrs={'class':'input--style-6'})
        self.fields['cochera'].widget = forms.CheckboxInput(attrs={'class':'form-input estilo_servicios'})
        self.fields['patio'].widget = forms.CheckboxInput(attrs={'class':'form-input estilo_servicios'})
        self.fields['mascotas'].widget = forms.CheckboxInput(attrs={'class':'form-input estilo_servicios'})
        self.fields['niños'].widget = forms.CheckboxInput(attrs={'class':'form-input estilo_servicios'})
        self.fields['superficie'].widget = forms.TextInput(attrs={'class':'input--style-6 form-input'})


class EditarPublicacion(forms.ModelForm):
    servicios = forms.ModelMultipleChoiceField(queryset=Servicios.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)
    tipo_inmueble = forms.ModelChoiceField(queryset=Tipo_Inmueble.objects.all(), widget=forms.Select(attrs={'class':'form-control'}),required=False)
    ubicacion = forms.ModelChoiceField(queryset=Zona.objects.all(), widget=forms.Select(attrs={'class':'form-control'}), required=False)

    class Meta:
        model = Publicaciones
        fields = '__all__'
        exclude = ['publicacion_id']

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].widget = forms.TextInput(attrs={'class':'input--style-6'})
        self.fields['precio'].widget = forms.NumberInput(attrs={'class':'input--style-6'})
        self.fields['descripcion'].widget = forms.Textarea(attrs={'class':'textarea--style-6'})
        self.fields['ambientes'].widget = forms.NumberInput(attrs={'class':'input--style-6'})
        self.fields['habitaciones'].widget = forms.NumberInput(attrs={'class':'input--style-6'})
        self.fields['baños'].widget = forms.NumberInput(attrs={'class':'input--style-6'})
        self.fields['cochera'].widget = forms.CheckboxInput(attrs={'class':'form-input estilo_servicios'})
        self.fields['patio'].widget = forms.CheckboxInput(attrs={'class':'form-input estilo_servicios'})
        self.fields['mascotas'].widget = forms.CheckboxInput(attrs={'class':'form-input estilo_servicios'})
        self.fields['niños'].widget = forms.CheckboxInput(attrs={'class':'form-input estilo_servicios'})
        self.fields['superficie'].widget = forms.TextInput(attrs={'class':'input--style-6 form-input'})