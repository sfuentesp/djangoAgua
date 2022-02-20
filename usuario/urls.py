
from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="home"),

    path('login/', views.login, name="login"),
    #path('contacto/', views.contacto, name="contacto"),
    path('info/', views.info, name="info"),
    path('galeria/', views.galeria, name="galeria"),

    path('nuevousuarioDjangousu/', views.crearusuario,name="nuevo-usu-django"),
    path('nuevousuarioAppusu/', views.nuevoUsuario,name="nuevo-usu-app"),

    path('usuarios/', views.listarUser,name="listado-usu"),
    path('bienvenido/', views.bienvenido, name="home-bienvenido"),
    path('logout/',views.salir, name="salir-usu"),
   
    path('post/',views.nuevoPost, name="post-usu"),
    path('post/listado',views.listarPost, name="post-list-usu"),
]