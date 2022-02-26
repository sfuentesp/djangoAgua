
from django.urls import path
from . import views

urlpatterns=[
   
    path('boleta/', views.nuevaBoleta, name="boleta-usu"),
    path('boleta/listado', views.listarBoletas, name="boleta-listado-usu"),
    path('boleta/descarga/<str:nombre>', views.descargarDoc, name="boleta-descargar-usu"),
]