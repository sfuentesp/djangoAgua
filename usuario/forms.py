
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Usuario,Post
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#        model = User
#        fields =  ['username','email','password1','password2']


#clase para mostrar formulario del Modelo usuario
class UsuarioForm(forms.ModelForm): 
    class Meta: 
        password = forms.CharField(widget=forms.PasswordInput) 
        model=Usuario 
        fields=("rut","nombre","apellido","tipousu","password")
        widgets = { 'password': forms.PasswordInput(), } 
        
class LoginForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)

#clase para mostrar formulario para user de django
class UserForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    email=forms.CharField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('titulo','descripcion')




    