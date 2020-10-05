from .models import Perfil
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from apps.usuarios.models import Usuario


class RegistroUsuario(UserCreationForm):
    telefono = forms.CharField(max_length=20)
    descripcion = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()
    facebook = forms.CharField(max_length=255, required=False)
    instagram = forms.CharField(max_length=255, required=False)
    twitter = forms.CharField(max_length=255, required=False)
    pinterest = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'propietario']

    @transaction.atomic
    def save(self):
        usuario = super().save()
        Perfil.objects.create(usuario_id=usuario, telefono= self.cleaned_data.get('telefono'), 
                                descripcion= self.cleaned_data.get('descripcion'), 
                                imagen= self.cleaned_data.get('imagen'), facebook=self.cleaned_data.get('facebook'),
                                instagram=self.cleaned_data.get('instagram'), twitter=self.cleaned_data.get('twitter'), 
                                pinterest=self.cleaned_data.get('pinterest'))

        return usuario

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class':'form-input'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-input'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-input'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class':'form-input'})
        self.fields['telefono'].widget = forms.NumberInput(attrs={'class':'form-input'})
        self.fields['descripcion'].widget = forms.Textarea(attrs={'class':'textarea--style-6 form-input'})
        self.fields['imagen'].widget = forms.FileInput(attrs={'class':'input-group js-input-file'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-input'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-input'})
        self.fields['propietario'].widget = forms.CheckboxInput(attrs={'class':'agree-term'})

        self.fields['facebook'].widget = forms.TextInput(attrs={'class':'form-input'})
        self.fields['instagram'].widget = forms.TextInput(attrs={'class':'form-input'})
        self.fields['twitter'].widget = forms.TextInput(attrs={'class':'form-input'})
        self.fields['pinterest'].widget = forms.TextInput(attrs={'class':'form-input'})

class EditarPerfil(forms.ModelForm):
    telefono = forms.CharField(max_length=20)
    descripcion = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()
    facebook = forms.CharField(max_length=255, required=False)
    instagram = forms.CharField(max_length=255, required=False)
    twitter = forms.CharField(max_length=255, required=False)
    pinterest = forms.CharField(max_length=255, required=False)
    
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email' ]

    @transaction.atomic
    def save(self):
        usuario = super().save(commit=False)
        usuario.perfilUsuario.telefono = self.cleaned_data.get('telefono')
        usuario.perfilUsuario.descripcion = self.cleaned_data.get('descripcion')
        usuario.perfilUsuario.imagen = self.cleaned_data.get('imagen')

        usuario.perfilUsuario.facebook = self.cleaned_data.get('facebook')
        usuario.perfilUsuario.instagram = self.cleaned_data.get('instagram')
        usuario.perfilUsuario.twitter = self.cleaned_data.get('twitter')
        usuario.perfilUsuario.pinterest = self.cleaned_data.get('pinterest')
        usuario.perfilUsuario.save()
        usuario.save()
        return usuario

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefono'].initial = kwargs['instance'].perfilUsuario.telefono
        self.fields['descripcion'].initial = kwargs['instance'].perfilUsuario.descripcion
        self.fields['imagen'].initial = kwargs['instance'].perfilUsuario.imagen
        self.fields['first_name'].widget = forms.TextInput(attrs={'class':'input--style-6'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class':'input--style-6'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class':'input--style-6'})
        self.fields['telefono'].widget = forms.NumberInput(attrs={'class':'input--style-6'})
        self.fields['descripcion'].widget = forms.Textarea(attrs={'class':'textarea--style-6'})
        self.fields['imagen'].widget = forms.FileInput(attrs={'class':'input-group js-input-file'})

        self.fields['facebook'].widget = forms.TextInput(attrs={'class':'input--style-6'})
        self.fields['instagram'].widget = forms.TextInput(attrs={'class':'input--style-6'})
        self.fields['twitter'].widget = forms.TextInput(attrs={'class':'input--style-6'})
        self.fields['pinterest'].widget = forms.TextInput(attrs={'class':'input--style-6'})