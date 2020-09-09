from django.shortcuts import render
from django.views.generic import CreateView, DeleteView 
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .forms import *
from .models import Publicaciones, Imagenes_Publicaciones
from django.urls import reverse_lazy
from django.forms import formset_factory


def Publicacion(request):	
	return render(request,'publicacion/publicacion.html')

def CargarImagenes(request):
	return render(request, 'publicacion/publicacion.html')

class Crear(CreateView):
	model = Publicaciones
	form_class = AltaPublicacion
	template_name = 'publicacion/crear.html'
	success_url = reverse_lazy('home')

class Editar(UpdateView):
	model = Publicaciones
	form_class = EditarPublicacion
	template_name = "publicacion/editar.html"
	success_url = reverse_lazy('home')


class Borrar(DeleteView):
	model = Publicaciones
	success_url = reverse_lazy("propiedades.html")

class ListarPublicaciones(ListView):
	model = Publicaciones
	template_name = 'propiedades.html'
"""
def post(request):

       ImageFormSet = modelformset_factory(Imagenes_Publicaciones,
                                           form=ImagenesForm, extra=1)

       if request.method == 'POST':

           postForm = AltaPublicacion(request.POST)
           formset = ImageFormSet(request.POST, request.FILES,
                                  queryset=Imagenes_Publicaciones.objects.none())


           if postForm.is_valid() and formset.is_valid():



               post_form = postForm.save(commit=False)
               post_form.user = request.user
               post_form.save()

               for form in formset.cleaned_data:
                   image = form['image']
                   photo = Images(post=post_form, image=image)
                   photo.save()
               messages.success(request,
                                "Yeeew,check it out on the home page!")
               return HttpResponseRedirect("publicacion/publicacion.html")
           else:
               print (postForm.errors, formset.errors)
       else:
           postForm = PostForm()
           formset = ImageFormSet(queryset=Imagenes_Publicaciones.objects.none())
       return render(request, 'publicacion/crear.html',
                     {'postForm': postForm, 'formset': formset},
                     context_instance=RequestContext(request))

"""