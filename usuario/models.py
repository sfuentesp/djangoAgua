from django.db import models
from django.forms import CharField

# Create your models here.

class Usuario(models.Model):
    rut=models.CharField(max_length=10,null=False)
    nombre=models.CharField(max_length=50,null=False)
    apellido=models.CharField(max_length=100,null=False)
    tipousu=models.CharField(max_length=100, null=False)
    


