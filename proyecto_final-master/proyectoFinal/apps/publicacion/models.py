from django.db import models


class Servicios(models.Model):
    nombre = models.CharField(max_length=50, default=False)

    def __str__(self):
        return self.nombre


class Tipo_Inmueble(models.Model):
    nombre = models.CharField(max_length=50, default=False)

    def __str__(self):
        return self.nombre


class Publicaciones(models.Model):
    publicacion_id = models.AutoField(primary_key=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length= 100)
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


#ARREGAR SERVICIOS, TIPO DE INMUEBLE Y AGREGAR FECHA DE PUBLICACION AL MODEL, AGREGAR UNA CLASS ZONA

class Imagenes_Publicaciones(models.Model):
    img = models.ImageField(upload_to= "publicaciones", null=False, blank=False)
    publicacion = models.ForeignKey(Publicaciones,related_name='imgInmueble', null=True, on_delete=models.SET_NULL)#me parece que esto no va...