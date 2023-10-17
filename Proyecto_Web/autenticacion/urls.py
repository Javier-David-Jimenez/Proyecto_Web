"""Una vez generado el archivo urls.py dentro de la aplicacion importamos el path 
y las views de la app generamos un urlpatterns y pongo los paths del proyecto"""

from django.urls import path
from .views import Vregistro, cerrar_sesion, logear


urlpatterns = [
  
    path('', Vregistro.as_view(), name='Autenticacion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path('logear', logear, name='logear'),
    
]
