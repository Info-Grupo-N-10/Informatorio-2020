from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .filters import FiltroPublicacion

app_name="publicacion"

urlpatterns = [

	path('Publicacion/<int:pk>/', views.Publicacion, name='public'),
	path('Propiedades/', views.ListarPublicaciones.as_view(), name='propiedades'),
	path('Crear/', views.Crear.as_view(), name="crear"),
	path('Borrar/<int:pk>/', views.Borrar.as_view(), name="borrar"),
	path('Editar/<int:pk>/', views.Editar.as_view(), name="editar"),
	path('Buscar/', views.Filtros, name='filtrado')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)