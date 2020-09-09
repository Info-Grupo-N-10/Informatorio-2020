from django.contrib import admin

from django.contrib import admin
from .models import *



admin.site.register(Servicios)

admin.site.register(Tipo_Inmueble)

class PublicacionesImagenes(admin.TabularInline):
    model = Imagenes_Publicaciones
    extra = 1
class PublicacionAdmin(admin.ModelAdmin):
    inlines = [ PublicacionesImagenes, ]


admin.site.register(Publicaciones, PublicacionAdmin)