from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ubicacion
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UbicacionForm


def mostrarMapa(request, pk):
    m = Ubicacion.objects.get(publicacion=pk)

    context = {
    'lat': m.lat,
    'lng': m.lng, }
    print(context)

    return render(request, 'publicacion/publicacion.html', context)


class CrearMapa(CreateView):
	model = Ubicacion
	form_class = UbicacionForm
	template_name = 'mapas/mapas.html'
	success_url = reverse_lazy('publicacion:propiedades')

	# def form_valid(self, form):
	# 	m = form.save(commit=False)
	# 	m.instance.publicacion = self.kwargs['publicacion_id']
	# 	m.save()
	# 	return redirect(self.success_url)
   