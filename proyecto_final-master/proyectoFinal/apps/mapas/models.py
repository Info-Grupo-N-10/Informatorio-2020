from django.db import models
from apps.publicacion.models import Publicaciones


class Ubicacion(models.Model):
	lat = models.CharField(max_length=50)
	lng = models.CharField(max_length=50)
	publicacion = models.OneToOneField(Publicaciones, related_name='mapaPublicacion', null=True, on_delete=models.CASCADE)

