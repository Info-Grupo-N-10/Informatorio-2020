from django.shortcuts import render

# Create your views here.

def Favoritos(request):
	return render(request, 'favoritos/favoritos.html')# esta vista tiene que accederser desde perfil