from django.shortcuts import render

# Create your views here.
def Perfiles(request):
	return render(request,'publicacion/perfiles.html')	

def Agente1(request):
	return render(request,'perfil/agente1.html')

def Agente2(request):
	return render(request,'perfil/agente2.html')

def Agente3(request):
	return render(request,'perfil/agente3.html')