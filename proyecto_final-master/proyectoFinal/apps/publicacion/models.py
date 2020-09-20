from django.db import models
from apps.usuarios.models import Usuario


class Servicios(models.Model):
	nombre = models.CharField(max_length=50, default=False)

	def __str__(self):
		return self.nombre
	

class Tipo_Inmueble(models.Model):
	nombre = models.CharField(max_length=50, default=False)

	def __str__(self):
		return self.nombre

class Zona(models.Model):
	ubicacion =  models.CharField(max_length= 100)

	def __str__(self):
		return self.ubicacion

class Publicaciones(models.Model):
	publicacion_id = models.AutoField(primary_key=True)
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	descripcion = models.TextField()
	ubicacion =  models.ForeignKey('Zona',related_name='zonaInmueble', null=True, on_delete=models.SET_NULL)
	ambientes = models.IntegerField()
	habitaciones = models.IntegerField()
	baños = models.IntegerField()
	cochera = models.BooleanField(default=False)
	patio = models.BooleanField(default=False)
	mascotas = models.BooleanField(default=False)
	niños = models.BooleanField(default=False)
	superficie = models.CharField(max_length= 50)
	servicios = models.ManyToManyField(Servicios, related_name='miServicios')
	tipo_inmueble = models.ForeignKey('Tipo_Inmueble',related_name='tipoInmueble', null=True, on_delete=models.SET_NULL)
	usuario = models.ForeignKey(Usuario , related_name="usuarioPublicacion", null=True, on_delete=models.CASCADE)

	


class Imagenes_Publicaciones(models.Model):
	img= models.ImageField(upload_to= "publicaciones", null=False, blank=False)
	publicaciones = models.ForeignKey(Publicaciones, related_name='imgPublicacion', null=True, on_delete=models.SET_NULL)

	
	

#ARREGAR SERVICIOS, TIPO DE INMUEBLE Y AGREGAR FECHA DE PUBLICACION AL MODEL, AGREGAR UNA CLASS ZONA

	
# def current_user(request):
	
# 		current_user = self.request.user
# 		publiacion.usuario = current_user.id
		

# 		return publicacion.usuario