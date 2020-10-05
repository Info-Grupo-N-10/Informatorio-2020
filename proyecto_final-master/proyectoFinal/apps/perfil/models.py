from django.db import models
from django.urls import reverse
from apps.usuarios.models import Usuario

class Perfil(models.Model):
    telefono = models.CharField(max_length=20)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to= "perfiles", null=True, blank=True)
    usuario_id = models.OneToOneField(Usuario , related_name="perfilUsuario", null=True, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    pinterest = models.CharField(max_length=255, null=True, blank=True)


    def getUsuario(self):
         return self.usuario_id
