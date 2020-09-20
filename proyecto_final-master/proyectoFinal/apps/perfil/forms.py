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
		usuario.save()
		Perfil.objects.create(usuario_id=usuario, telefono= self.cleaned_data.get('telefono'), 
								descripcion= self.cleaned_data.get('descripcion'), 
								imagen= self.cleaned_data.get('imagen'))
			 
		return usuario




class EditarPerfil(forms.ModelForm):
    telefono = forms.CharField(max_length=20)
    descripcion = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email' ]

    @transaction.atomic
    def save(self):
        usuario = super().save(commit=False)
        usuario.perfilUsuario.telefono = self.cleaned_data.get('telefono')
        usuario.perfilUsuario.descripcion = self.cleaned_data.get('descripcion')
        usuario.perfilUsuario.imagen = self.cleaned_data.get('imagen')
        usuario.perfilUsuario.save()
        usuario.save()
        return usuario

    def __init__(self,*args,**kwargs):
        super().__init__(args, kwargs)
        self.fields['telefono'].initial = kwargs['instance'].perfilUsuario.telefono
        self.fields['descripcion'].initial = kwargs['instance'].perfilUsuario.descripcion
        self.fields['imagen'].initial = kwargs['instance'].perfilUsuario.imagen



  

