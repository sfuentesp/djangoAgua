
from django import forms
from .models import Boleta
from django.db.models import fields



class FormBoleta(forms.ModelForm):
    class Meta:
        model=Boleta
        fields=('fecha_emision','mts3','upload','comentario')



