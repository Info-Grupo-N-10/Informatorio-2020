from django.db import models


class Servicios(models.Model):
    nombre = models.CharField(max_length=50, default=False)

    def __str__(self):
        return self.nombre
    
    # def getServicio(self):
    #     return self.miServicios


class Zona(models.Model):
    ubicacion =  models.CharField(max_length= 100)

    def __str__(self):
        return self.ubicacion

class Tipo_Inmueble(models.Model):
    nombre = models.CharField(max_length=50, default=False)

    def __str__(self):
        return self.nombre

    # def getInmueble(self):
    #     return self.tipoInmueble


class Publicaciones(models.Model):
    publicacion_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
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
    tipo_inmueble = models.ForeignKey('Tipo_Inmueble', related_name='tipoInmueble', null=True, on_delete=models.SET_NULL)

    def getImagen(self):
        print(self.imgInmueble.all())
        if self.imgInmueble.all():
            return self.imgInmueble.all()[0]
        else:
            return None

    def mostrarTodas(self):
        if self.imgInmueble.all():
            return self.imgInmueble.all()
        else:
            return None
    

#ARREGAR SERVICIOS, TIPO DE INMUEBLE Y AGREGAR FECHA DE PUBLICACION AL MODEL, AGREGAR UNA CLASS ZONA

class Imagenes_Publicaciones(models.Model):
    img = models.ImageField(upload_to= "publicaciones", null=False, blank=False)
    publicacion = models.ForeignKey(Publicaciones,related_name='imgInmueble', null=True, on_delete=models.SET_NULL)#me parece que esto no va...
    
    # def getImagen(self):
    #     return self.imgInmueble

    # def getPublicacion(self):
    #     return self.publicacion