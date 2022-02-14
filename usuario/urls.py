from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="home"),

    path('login/', views.login, name="login"),
    path('contacto/', views.contacto, name="contacto"),
    path('info/', views.info, name="info"),
    path('galeria/', views.galeria, name="galeria"),

    path('nuevousuario/', views.nuevoUsuario,name="nuevo-usu"),
    path('usuarios/', views.listarUser,name="listado-usu"),
    path('bienvenido/', views.bienvenido),
    path('logout/',views.salir, name="salir-usu"),
   
    
    
]