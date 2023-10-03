from django.db import models

# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(max_length = 50)
    contenido = models.CharField(max_length = 90)
    imagen = models.ImageField(upload_to='media/servicios')
    # el (auto_now_add=True) es para coger la fecha y hora de modificación
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        
    def __str__(self):
        return self.titulo