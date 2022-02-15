import email
from django.shortcuts import redirect, render
from .models import Usuario
from .forms import UsuarioForm, LoginForm,UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


from .backend import MyBackend
myBackend=MyBackend()

def home(request):
    return render(request,'usuario/index.html')

def contacto(request):
    return render(request,'usuario/contacto.html')

def info(request):
    return render(request,'usuario/info.html')

def galeria(request):
    return render(request,'usuario/galeria.html')


def listarUser(request):
    usu=Usuario.objects.all()
    usu2=User.objects.all()
    return render(request,'usuario/usuarios.html',{"usu":usu,"usu2":usu2})


def nuevoUsuario(request):
    if request.method=="POST":
        form=UsuarioForm(data= request.POST)
        if form.is_valid():
            cliente=form.save(commit=False)
            cliente.save() #se guarda en la db
                  
        return redirect('/usuarios')

    else:
        form=UsuarioForm()
        return render(request,'usuario/nuevousuarioAppusuario.html',{"form":form})



def crearusuario(request):
    #dinamico
    if request.method=="POST":
        form=UserForm(data= request.POST)
        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            email=form.cleaned_data["email"]
            clave=form.cleaned_data["password"]
            
            user=User.objects.create_user(nombre,email,clave)
           
            user.save()
        return redirect('/login')
    else:
        form=UserForm()
        return render(request,'usuario/nuevousuario.html',{"form":form})
        

def login(request):
    if request.method=="POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():

            nombre=form.cleaned_data["nombre"]
            clave=form.cleaned_data["password"]
            user=authenticate(request,username=nombre,password=clave)
            
            print(user)
            if user is not None:
               auth_login(request,user)
                
        return render(request,'usuario/bienvenido.html',{"user":user})
      
    else:
        form=LoginForm()
        return render(request,'usuario/login.html',{"form":form})



def login2(request):
    if request.method=="POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():

            rut=form.cleaned_data["rut"]
            clave=form.cleaned_data["password"]
            user=myBackend.authenticate(request,username=rut,password=clave)
            
            print(user)
            if user is not None:
               # auth_login(request,user)
                login(request, user)
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