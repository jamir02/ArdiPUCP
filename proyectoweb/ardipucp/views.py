from django.shortcuts import render
from django.http import HttpResponse
from .models import usuario
from .models import productos
from .models import promociones
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

def promociones_1(request):
    usuarios_totales = usuario.objects.all()
    promociones_totales = promociones.objects.all() 
    return render(request,"ardipucp/promociones.html",{
        'usuarios_totales': usuarios_totales,
        'promociones_totales': promociones_totales
    })


def eliminar_producto(request,ind):
    producto_eliminar = productos.objects.get(id=ind)#Obtengo la tarea seleccionada por id 
    producto_eliminar.delete() #Elimino la tarea seleccionada de la base de datos
    return HttpResponseRedirect(reverse("ardipucp:stock"))#Redirecciono a la vista de dashboard

def añade_producto(request):
    usuarios_totales = usuario.objects.all()

    if request.method == "POST":
        categoriaproducto= request.POST.get('categoriaproducto')#Recibo el titulo de la nueva tarea
        nombreproduct= request.POST.get('nombreproduct')#Recibo la descripcion de la nueva tarea
        image_name= request.POST.get('image_name') #Recibo la fecha de la creacion de la nueva tarea
        precio_producto= request.POST.get('precio_producto') #Recibo la fecha de entrega de la nueva tarea
        stock_producto= request.POST.get('stock_producto') #Recibo el usuario designado de la nueva tarea 
        descripcion_producto= request.POST.get('descripcion_producto') #Recibo el usuario designado de la nueva tarea 
        #print(str(categoriaproducto))
        #print(str(nombreproduct))
        #print(str(image_name))
        #print(str(precio_producto))
        #print(str(stock_producto))
        #print(str(descripcion_producto))
        productos(categoria=str(categoriaproducto), producto=str(nombreproduct),imagen=str(image_name),precio=str(precio_producto),stock=str(stock_producto), descripcion=str(descripcion_producto)).save()

    return render(request,"ardipucp/añade_producto.html",{
        'usuarios_totales': usuarios_totales
    })

def edita_stock(request, ind):
    usuarios_totales = usuario.objects.all()
    producto_seleccionado=productos.objects.get(id=ind)

    if request.method == "POST":
        stockproducto_2= request.POST.get('stock_producto_2')#Recibo el titulo de la nueva tarea
        stock_eliminar = productos.objects.get(id=ind)#Obtengo la tarea seleccionada por id 
        stock_eliminar.stock= stockproducto_2
        stock_eliminar.save() #Elimino la tarea seleccionada de la base de datos
        #print(stockproducto_2)
    return render(request,"ardipucp/vista_producto.html",{
        'usuarios_totales': usuarios_totales,
        'producto_seleccionado': producto_seleccionado
    })

def añade_promocion(request):
    usuarios_totales = usuario.objects.all()
    promociones_totales = promociones.objects.all()
    if request.method == "POST":
        nombreproducto= request.POST.get('nombreproducto')#Recibo el titulo de la nueva tarea
        nombrepromo= request.POST.get('nombrepromo')#Recibo la descripcion de la nueva tarea
        tipopromo= request.POST.get('tipopromo') #Recibo la fecha de la creacion de la nueva tarea
        grupousuario= request.POST.get('grupousuario') #Recibo la fecha de entrega de la nueva tarea
        preciopromo= request.POST.get('preciopromo') #Recibo el usuario designado de la nueva tarea 
        duraciónpromo= request.POST.get('duraciónpromo') #Recibo el usuario designado de la nueva tarea 
        #print(str(nombreproducto))
        #print(str(nombrepromo))
        #print(str(tipopromo))
        #print(str(grupousuario))
        #print(str(preciopromo))
        #print(str(duraciónpromo))
        promociones(producto=str(nombreproducto), nombre=str(nombrepromo),tipo=str(tipopromo),condición=str(grupousuario),precio=str(preciopromo), duración=str(duraciónpromo)).save()
        
    return render(request,"ardipucp/añade_promocion.html",{
        'usuarios_totales': usuarios_totales,
        'promociones_totales': promociones_totales
    })

def eliminar_promocion(request,ind):
    promocion_eliminar = promociones.objects.get(id=ind)#Obtengo la tarea seleccionada por id 
    promocion_eliminar.delete() #Elimino la tarea seleccionada de la base de datos
    return HttpResponseRedirect(reverse("ardipucp:promociones_1"))#Redirecciono a la vista de dashboard

