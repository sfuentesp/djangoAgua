
from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

class Boleta(models.Model):
    fecha_emision=models.DateField("Fecha de emisión boleta", null=False)
    mts3=models.DecimalField("m3 facturados (consumo del mes)",max_digits=5, decimal_places=2, null=False)
    monto_facturado=models.IntegerField(null=False)
    fecha_ingreso=models.DateTimeField(auto_now_add=True)
    upload = models.FileField("Ingresar boleta (formato pdf, jpg o png)", null=True, blank=True)
    comentario=models.TextField("¿Cuéntanos cómo lo estás haciendo?", null=False)
    usu = models.ForeignKey(User, on_delete=models.CASCADE)
