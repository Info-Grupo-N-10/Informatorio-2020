from django.db import models



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
	servicios = models.ForeignKey(
        'Servicios', on_delete=models.CASCADE)
	tipo_inmueble = models.ForeignKey('Tipo_Inmueble', on_delete=models.CASCADE)

class Servicios(models.Model):
	internet = models.BooleanField(default=False) 
	cable = models.BooleanField(default=False)
	luz = models.BooleanField(default=False)
	telefono = models.BooleanField(default=False)

class Tipo_Inmueble(models.Model):
	casa = models.BooleanField(default=False)
	departamento = models.BooleanField(default=False)
	duplex = models.BooleanField(default=False)
	habitacion = models.BooleanField(default=False)


#ARREGAR SERVICIOS, TIPO DE INMUEBLE Y AGREGAR FECHA DE PUBLICACION AL MODEL, AGREGAR UNA CLASS ZONA

