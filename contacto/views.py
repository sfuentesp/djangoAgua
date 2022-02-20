from django.shortcuts import redirect, render
from .forms import FormContacto,FormGestionado
from .models import Contacto
from django.contrib.auth.decorators import login_required
# Create your views here.
def nuevoContacto(request):
    if request.method=="POST":
        form=FormContacto(data= request.POST)
        if form.is_valid():
            contacto=form.save(commit=False)
            contacto.save() #se guarda en la db
                  
        return render(request,'usuario/contactoV2.html',{"mensaje":1})
        
    else:
        form=FormContacto()
        return render(request,'usuario/contactoV2.html',{"form":form})


@login_required(login_url="/login")
def listarContactos(request):
    c=Contacto.objects.order_by('-fecha')
    
    return render(request,'contacto/contactos.html',{"contactos":c})


@login_required(login_url="/login")
def eliminarContacto(request,id):
    c=Contacto.objects.get(pk=id)
    c.delete()
    return redirect(listarContactos)

@login_required(login_url="/login")
def gestionarRegistro(request,id):
    c=Contacto.objects.get(pk=id)
    form=FormGestionado(instance=c)

    if request.method=="POST":
        form=FormGestionado(data=request.POST, instance=c)
        form.save()
        return redirect(listarContactos)
    else:
       
        return render(request,'contacto/gestionar.html',{"form":form,"c":c})
