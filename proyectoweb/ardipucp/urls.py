from . import views
from django.urls import path

app_name= 'ardipucp'

urlpatterns = [
    path("", views.index,name="index"),
    path("dashboard",views.dashboard,name= "dashboard"),
    path("dashboard/stock",views.stock,name= "stock"),
    path("dashboard/analiticas",views.analiticas,name= "analiticas"),
    path("dashboard/promociones",views.promociones,name= "promociones"),
    path("dashboard/configuracion",views.configuracion,name= "configuracion"),
    path("dashboard/stock/eliminar_producto/<str:ind>", views.eliminar_producto, name="eliminar_producto"),
    path("dashboard/stock/añade_producto", views.añade_producto, name="añade_producto"),
    path("dashboard/stock/edita_stock", views.edita_stock, name="edita_stock")
]