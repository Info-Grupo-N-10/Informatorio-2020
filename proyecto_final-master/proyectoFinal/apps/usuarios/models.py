from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    propietario = models.BooleanField(default= False)

    def getPerfil(self):
        return self.perfilUsuario