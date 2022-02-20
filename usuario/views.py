from datetime import datetime
from django.shortcuts import redirect, render
from .models import Usuario, Post
from .forms import PostForm, UsuarioForm, LoginForm,UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


from .backend import MyBackend
myBackend=MyBackend()

def home(request):
    return render(request,'usuario/index.html')



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
            
            usu=form.cleaned_data["nombre"]
            clave=form.cleaned_data["password"]
            user=authenticate(request,username=usu,password=clave)
           
            if user is not None:
                auth_login(request,user)
                #return render(request,'usuario/bienvenida.html',{"user":user})
                return redirect("/bienvenido")
            else:
                return redirect("/login")
           
    else:
        form=LoginForm()
        return render(request,'usuario/login.html',{"form":form})


@login_required(login_url="/login")
def bienvenido(request):
    return render(request,'usuario/bienvenido.html')

def salir(request):
    logout(request)
    return redirect("/bienvenido")


@login_required(login_url="/login")
def nuevoPost(request):
    if request.method=="POST":
        form=PostForm(data= request.POST)
        if form.is_valid():
            titulos=form.cleaned_data["titulo"]
            des=form.cleaned_data["descripcion"]
          
            usu=request.user

            post=Post.objects.create(titulo=titulos, descripcion=des, autor=usu)
           
        return redirect(listarPost)
        
    else:
        form=PostForm()
        return render(request,'usuario/post.html',{"form":form})

@login_required(login_url="/login")
def listarPost(request):
    post=Post.objects.filter(autor=request.user)
    
    return render(request,'usuario/post_list.html',{"posts":post})

def eliminarPost(request,id):
    post=Post.objects.get(pk=id)
    post.delete()
    return redirect(listarPost)

def editarPost(request,id):
    post=Post.objects.get(pk=id)
    form=PostForm(instance=post)

    if request.method=="POST":
        form=PostForm(data=request.POST, instance=post)
        form.save()
        return redirect(listarPost)
    else:
        
        return render(request,'usuario/editarPost.html',{"form":form})