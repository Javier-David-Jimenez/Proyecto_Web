"""Una vez generado el archivo urls.py dentro de la aplicacion importamos el path 
y las views de la app generamos un urlpatterns y pongo los paths del proyecto"""

from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='Home'),
    path('tienda', views.tienda, name='Tienda'),
    
]

#url para los archivos media para poder verlos durante el desarrollo. no apto para producción
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
