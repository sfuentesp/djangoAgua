import email
from django.shortcuts import redirect, render
from .models import Usuario
from .forms import UsuarioForm
# Create your views here.


def home(request):
    return render(request,'usuario/index.html')

def contacto(request):
    return render(request,'usuario/contacto.html')

def listarUser(request):
    usu=Usuario.objects.all()
    return render(request,'usuario/usuarios.html',{"usu":usu})


def nuevoUsuario(request):
    if request.method=="POST":
        form=UsuarioForm(data= request.POST)
        if form.is_valid():
            cliente=form.save(commit=False)
            cliente.save() #se guarda en la db
                  
        return redirect('/usuarios')

    else:
        form=UsuarioForm()
        return render(request,'usuario/nuevousuario.html',{"form":form})