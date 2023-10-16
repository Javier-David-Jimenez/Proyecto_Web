"""Una vez generado el archivo urls.py dentro de la aplicacion importamos el path 
y las views de la app generamos un urlpatterns y pongo los paths del proyecto"""

from django.urls import path
from . import views

app_name = "carro"
#usando el name space en la ruta evitamos la colision con nombres compartidos

urlpatterns = [

    path('agregar/<int:producto_id>/', views.agregar_producto, name="agregar"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="eliminar"),
    path('restar/<int:producto_id>/', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_carro, name="limpiar"),
]
