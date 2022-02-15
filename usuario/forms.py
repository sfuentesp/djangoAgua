
from django import forms
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
       model = User
       fields =  ['username','email','password1','password2']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=("rut","nombre","apellido","tipousu","password")

class LoginForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)

class UserForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    email=forms.CharField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)




    