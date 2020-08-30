from django.shortcuts import render

def Home(request):
	return render(request, 'home.html')#home

def Registro(request):
	return render(request, 'registro.html') #registro

def Usuarios(request):
	return render(request, 'usuarios.html')#usuarios

def Propiedades(request):
	return render(request, 'propiedades.html')#propiedades

def Contacto(request):
	return render(request, 'contacto.html')

def Perfiles(request):
	return render(request, 'perfiles.html')

#Registro, Perfil, Usuarios, Propiedades, Publicación, Favoritos