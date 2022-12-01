from django.shortcuts import render
from django.http import HttpResponse
from .models import usuario
from .models import productos
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

def stock(request):
    productos_totales = productos.objects.all() 
    usuarios_totales = usuario.objects.all()
    return render(request,"ardipucp/stock.html",{
        'usuarios_totales': usuarios_totales,
        'productos_totales': productos_totales
    })

def analiticas(request):
    usuarios_totales = usuario.objects.all()
    return render(request,"ardipucp/analiticas.html",{
        'usuarios_totales': usuarios_totales
    })

def promociones(request):
    usuarios_totales = usuario.objects.all()
    return render(request,"ardipucp/promociones.html",{
        'usuarios_totales': usuarios_totales
    })

def configuracion(request):
    usuarios_totales = usuario.objects.all()
    return render(request,"ardipucp/configuracion.html",{
        'usuarios_totales': usuarios_totales
    })

def eliminar_producto(request,ind):
    producto_eliminar = productos.objects.get(id=ind)#Obtengo la tarea seleccionada por id 
    producto_eliminar.delete() #Elimino la tarea seleccionada de la base de datos
    return HttpResponseRedirect(reverse("ardipucp:stock"))#Redirecciono a la vista de dashboard

def añade_producto(request):
    usuarios_totales = usuario.objects.all()
    return render(request,"ardipucp/añade_producto.html",{
        'usuarios_totales': usuarios_totales
    })

def edita_stock(request):
    usuarios_totales = usuario.objects.all()
    return render(request,"ardipucp/edita_stock.html",{
        'usuarios_totales': usuarios_totales
    })