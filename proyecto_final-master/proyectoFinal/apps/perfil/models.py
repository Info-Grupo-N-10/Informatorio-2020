from django.db import models
from django.urls import reverse
from apps.usuarios.models import Usuario

class Perfil(models.Model):
    telefono = models.CharField(max_length=20)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to= "perfiles", null=True, blank=True)
    perfilUsuario_id = models.OneToOneField(Usuario , related_name="perfilUsuario", null=True, on_delete=models.CASCADE)