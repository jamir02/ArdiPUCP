from django.shortcuts import render
from django.http import HttpResponse
from .models import usuario
#from .models import tarea
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

usuarios_totales = usuario.objects.all() 

def index(request):
    usuario = request.POST.get("usuario") # Obtengo el usuario de la vista
    contrasena = request.POST.get("contrasena") #Obtengo contraseña de la vista
    for each_usuario in usuarios_totales: # Comprueba para cada usuario
        if ((each_usuario.nombre == usuario) and (each_usuario.clave == contrasena)): # Compruebo credenciales
            print("Ingreso valido")
            print("El nombre de usuario es: " + str(usuario))
            print("La contraseña del usuario es: " + str(contrasena)) # Se immprime el usuario y contraseña
            return HttpResponseRedirect(reverse("ardipucp:dashboard")) #Voy a la vista dashboard
            
        return render(request,"ardipucp/ingreso.html") # Caso contrario retorna la vista de login 

def dashboard(request):
    usuarios_totales = usuario.objects.all()
    return render(request,"ardipucp/dashboard.html",{
        'usuarios_totales': usuarios_totales
    })