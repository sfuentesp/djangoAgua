from django.shortcuts import render
from .models import Usuario
# Create your views here.

def contacto(request):
    return render(request,'usuario/contacto.html')

def listarUser(request):
    usu=Usuario.objects.all()
    return render(request,'usuario/usuarios.html',{"usu":usu})