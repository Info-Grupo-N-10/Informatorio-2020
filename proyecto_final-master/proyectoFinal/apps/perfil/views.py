from django.shortcuts import render

# Create your views here.
def Perfil(request):
	return render(request,'perfil/perfil.html')

def Agente1(request):
	return render(request,'perfil/agente1.html')

def Agente2(request):
	return render(request,'perfil/agente2.html')

def Agente3(request):
	return render(request,'perfil/agente3.html')