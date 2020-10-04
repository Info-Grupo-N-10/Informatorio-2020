from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.Home, name = 'home'),
    path('Logout', auth.LogoutView.as_view(), name='logout'),
    path('Login',auth.LoginView.as_view(template_name="home.html"),name="login"),
    path('Terminos/', views.Terminos, name = 'terminos'),

    #urls otras app
    path('Perfil/', include('apps.perfil.urls')),
    path('Registro/', include('apps.usuarios.urls')),
    path('Inmuebles/', include('apps.publicacion.urls')),
    path('Favoritos/', include('apps.favoritos.urls')),
     path('Mapas/', include('apps.mapas.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)