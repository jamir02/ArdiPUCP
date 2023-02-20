from . import views
from django.urls import path

app_name= 'ardipucp'

urlpatterns = [
    path("", views.index,name="index"),
    path("dashboard",views.dashboard,name= "dashboard"),
    path("dashboard/stock",views.stock,name= "stock"),
    path("dashboard/analiticas",views.analiticas,name= "analiticas"),
    path("dashboard/promociones",views.promociones_1,name= "promociones_1"),
    path("dashboard/stock/eliminar_producto/<str:ind>", views.eliminar_producto, name="eliminar_producto"),
    path("dashboard/stock/añade_producto", views.añade_producto, name="añade_producto"),
    path("dashboard/stock/vista_producto/<str:ind>", views.edita_stock, name="vista_producto"),
    path("dashboard/stock/añade_promocion", views.añade_promocion, name="añade_promocion"),
    path("dashboard/promociones/eliminar_promocion/<str:ind>", views.eliminar_promocion, name="eliminar_promocion")
]