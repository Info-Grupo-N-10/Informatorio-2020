from django.db import models
from apps.usuarios.models import Usuario
from apps.publicacion.models import Publicaciones
from apps.perfil.models import Perfil 


class BaseFavorito(models.Model):
    usuario = models.ForeignKey(Usuario, verbose_name="usuario", related_name="favoritos", on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.usuario.username


class Favoritos(BaseFavorito):

    class Meta:
        db_table = "Favorito"

    objeto = models.ForeignKey(Publicaciones, verbose_name="Publicacion", related_name="favoritos", on_delete=models.CASCADE)

    def __unicode__(self):
    	return self.objeto.descripcion





