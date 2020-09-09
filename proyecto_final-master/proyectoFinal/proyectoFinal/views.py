from django.shortcuts import render

def Home(request):
	return render(request, 'home.html')#home

def Registro(request):
	return render(request, 'registro.html') #home

def Usuarios(request):
	return render(request, 'usuarios.html')#propiedades

#Registro, Perfil, Usuarios, Propiedades, Publicación, Favoritos