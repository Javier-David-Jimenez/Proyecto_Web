"""Una vez generado el archivo urls.py dentro de la aplicacion importamos el path 
y las views de la app generamos un urlpatterns y pongo los paths del proyecto"""

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#hemos copiado y pegado todos los path pero solo dejamos el de servicios y le  hacemso que a punte a'' (la raiz) en vez de a 'servicios'
    
urlpatterns = [
   
    path('', views.servicios, name='Servicios'),

]
