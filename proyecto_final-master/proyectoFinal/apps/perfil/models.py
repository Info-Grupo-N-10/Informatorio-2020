from django.db import models
from django.urls import reverse

class Perfil(models.Model):
	usuario_id = models.ForeignKey(
        'Usuario', on_delete=models.CASCADE)
	nombre = models.CharField(max_length= 80)
	telefono = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to= "productos", null=True, blank=True)



