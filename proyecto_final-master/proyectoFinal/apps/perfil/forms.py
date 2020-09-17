from .models import Perfil
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from apps.usuarios.models import Usuario


class RegistroUsuario(UserCreationForm):
    telefono = forms.CharField(max_length=20)
    descripcion = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'propietario']

    @transaction.atomic
    def save(self):
        usuario = super().save()
        Perfil.objects.create(usuario_id=usuario, telefono= self.cleaned_data.get('telefono'), 
                                descripcion= self.cleaned_data.get('descripcion'), 
                                imagen= self.cleaned_data.get('imagen'))

        return usuario

# class EditarPerfil(forms.ModelForm):

#     class Meta:
#         model = Usuario
#         fields = ['email', 'first_name', 'last_name','descr']






# from .models import Perfil
# from django import forms


# class AltaPerfil(forms.ModelForm):

#     class Meta:
#         model = Perfil
#         fields = '__all__'
#         exclude = ['perfilUsuario_id']


# class EditarPerfil(forms.ModelForm):
#      class Meta:
#          model = Perfil
#          fields =  ["nombre","apellido", "telefono", "email", "descripcion", "imagen"]