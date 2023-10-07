"""Una vez generado el archivo urls.py dentro de la aplicacion importamos el path 
y las views de la app generamos un urlpatterns y pongo los paths del proyecto"""

from django.urls import path
from . import views


urlpatterns = [
  
    path('', views.contacto, name='Contacto'),
    
]
