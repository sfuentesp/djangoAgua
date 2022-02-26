from encodings import normalize_encoding

from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import FormBoleta
from .models import Boleta
from django.contrib.auth.decorators import login_required
   
# Create your views here.
@login_required(login_url="/login")
def nuevaBoleta(request):
    if request.method=="POST":
        form=FormBoleta(request.POST,request.FILES or None )
     

        if form.is_valid():
            mes=form.cleaned_data["fecha_emision"].month
            ano= form.cleaned_data["fecha_emision"].year 

            busqueda=Boleta.objects.filter(usu=request.user).filter(fecha_emision__month=mes).filter(fecha_emision__year=ano)

            if not busqueda:
                form.instance.usu = request.user
                boleta=form.save(commit=False)
                boleta.save()
            else:
                mensaje=1
                return render(request,'boleta/boleta.html',{"form":form,"mensaje":mensaje})
         
                  
        return redirect(listarBoletas)
        
    else:
        form=FormBoleta()
        return render(request,'boleta/boleta.html',{"form":form})

@login_required(login_url="/login")
def listarBoletas(request):
    b=Boleta.objects.filter(usu=request.user).order_by("-fecha_emision")
    
    return render(request,'boleta/misBoletas.html',{"boletas":b})

def descargarDoc(request,nombre):

    ruta='boleta/static/uploads/'+str(nombre)
    f=open(ruta,'rb')
   
    response=HttpResponse(f.read(),content_type='application/pdf' )
    response['Content-Disposition'] = f'attachment; filename={nombre}' 

    return response
