
from django import forms
from .models import Contacto
from django.db.models import fields

class FormContacto(forms.ModelForm):
    class Meta:
        model=Contacto
        fields=("nombre","telefono","email","mensaje")


class FormGestionado(forms.ModelForm):
    class Meta:
        model=Contacto
        fields=("id","gestionado")
