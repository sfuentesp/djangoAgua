import email
from django.shortcuts import redirect, render
from .models import Usuario
from .forms import UsuarioForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
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



def login(request):
    if request.method=="POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():

            usu=form.cleaned_data["nombre"]
            clave=form.cleaned_data["password"]
            user=authenticate(request,username=usu,password=clave)
            print(user)
            if user is not None:
                auth_login(request,user)
        return render(request,'usuario/bienvenido.html',{"user":user})
    else:
        form=LoginForm()
        return render(request,'usuario/login.html',{"form":form})

@login_required(login_url="/login")
def bienvenido(request):
    return render(request,'usuario/bienvenido.html')

def salir(request):
    logout(request)
    return redirect("/bienvenido")