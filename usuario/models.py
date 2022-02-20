
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Usuario(models.Model):
    rut=models.CharField(max_length=10,null=False)
    nombre=models.CharField(max_length=50,null=False)
    apellido=models.CharField(max_length=100,null=False)
    tipousu=models.CharField(max_length=100,verbose_name="Tipo de Usuario", null=False)
    password=models.CharField(max_length=8)
    


class Post(models.Model):
    titulo=models.CharField(max_length=20, null=False)
    descripcion=models.TextField()
    fecha_publicacion = models.DateTimeField(default=datetime.datetime.now)
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE)


