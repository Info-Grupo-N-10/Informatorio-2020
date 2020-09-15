from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
# MI SUPER USER SE LLAMA guada PSSWORD guada
class Usuario(AbstractUser):
	def getPerfil(self):
		return self.perfilUsuario