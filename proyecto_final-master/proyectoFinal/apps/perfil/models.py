from django.db import models
from django.urls import reverse
from apps.usuarios.models import Usuario

class Perfil(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length= 80)
    apellido = models.CharField(max_length= 80)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to= "perfiles", null=True, blank=True)
    perfilUsuario_id = models.ForeignKey(Usuario , related_name="perfilUsuario", null=True, on_delete=models.CASCADE)