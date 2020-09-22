from django.shortcuts import render
from apps.publicacion.models import Publicaciones
from django.views.generic.list import ListView
from .models import Favoritos
import json
from django.http import HttpResponse


def Marcador(request, pk):

    favoritos, created = Favoritos.objects.get_or_create(usuario = request.user, objeto_id=pk)

    datos = {}

    datos['creado'] = "Fav creado exitosamente"
    datos['resultado'] = created,
    datos['favoritospk'] = favoritos.pk

    if not created:
        favoritos.delete()
        print("eliminado")

    if created:
        print("creado") 

    return HttpResponse(json.dumps(datos), content_type='application/json')

def lista_de_favoritos(request):
    queryset = request.user.favoritos.all()

    context = {'favoritos': queryset}

    return render(request, "favoritos/favoritos.html", context)


class lista_perfiles_favoritos(ListView):
    model = Favoritos
    template_name = 'favoritos/publicaciones_favs.html'