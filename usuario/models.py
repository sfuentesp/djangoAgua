
import email
from re import T
from xml.parsers.expat import model
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



class Responsabilidad(models.Model):
    nombre=models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nombre


class Voluntario(models.Model):
    rut=models.CharField(max_length=12, primary_key=True)
    nombre=models.CharField(max_length=60, null=False)
    email=models.EmailField(max_length=80, null=False)
    telefono=models.IntegerField(null=False)
    responsabilidad=models.ForeignKey(Responsabilidad,null=True, on_delete=models.SET_NULL)