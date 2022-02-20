
from django.urls import path
from . import views

urlpatterns=[
   
    path('contacto/', views.nuevoContacto, name="contacto"),
    path('contacto/registros', views.listarContactos, name="contacto-registros"),
    path('contacto/eliminar/<int:id>/', views.eliminarContacto),
    path('contacto/editar/<int:id>/', views.gestionarRegistro),
]