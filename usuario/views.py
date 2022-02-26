from datetime import datetime
from django.shortcuts import redirect, render
from .models import Usuario, Post, Voluntario, Responsabilidad
from boleta.models import Boleta
from .forms import PostForm, ResponsabilidadForm, UsuarioForm, LoginForm,UserForm, VoluntarioForm
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
    labels = []
    data = []

    queryset = Boleta.objects.order_by('-fecha_emision')[:5]
    for b in queryset:
        labels.append(b.comentario)
        data.append(b.mts3)

    return render(request, 'usuario/bienvenido.html', {
        'labels': labels,
        'data': data,
        })
    #return render(request,'usuario/bienvenido.html')

def salir(request):
    logout(request)
    return redirect("/bienvenido")


@login_required(login_url="/login")
def nuevoPost(request):
    if request.method=="POST":
        form=PostForm(data= request.POST)
        if form.is_valid():
            form.instance.autor = request.user
       
            post=form.save(commit=False)
            post.save() #se guarda en la db
            # titulos=form.cleaned_data["titulo"]
            # des=form.cleaned_data["descripcion"]
          
            # usu=request.user

            # post=Post.objects.create(titulo=titulos, descripcion=des, autor=usu)
           
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



@login_required(login_url="/login")
def nuevoVoluntario(request):
    v=Voluntario.objects.all()
 
    if request.method=="POST":
        form=VoluntarioForm(data= request.POST)
        if form.is_valid():
            volu=form.save(commit=False)
            volu.save() #se guarda en la db
        return redirect(nuevoVoluntario)
        
    else:
        form=VoluntarioForm()
        return render(request,'usuario/nuevoVoluntario.html',{"form":form,"v":v})

@login_required(login_url="/login")
def nuevaResponsabilidad(request):
    r=Responsabilidad.objects.all()
 
    if request.method=="POST":
        form=ResponsabilidadForm(data= request.POST)
        if form.is_valid():
            res=form.save(commit=False)
            res.save() #se guarda en la db
        return redirect(nuevaResponsabilidad)
        
    else:
        form=ResponsabilidadForm()
        return render(request,'usuario/nuevaResponsabilidad.html',{"form":form,"res":r})



