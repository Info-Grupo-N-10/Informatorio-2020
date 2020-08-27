from django.shortcuts import render

# Create your views here.
def Perfil(request):
	return render(request,'perfil/perfil.html')