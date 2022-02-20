import email
from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    telefono=models.CharField("Teléfono",max_length=12)
    fecha = models.DateTimeField(auto_now_add=True)
    email=models.EmailField(max_length=100)
    gestionado=models.BooleanField("Cerrar",default=False)
    mensaje=models.TextField()
