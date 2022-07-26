from cProfile import label
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class ProductosFormulario(forms.Form):
    producto = forms.CharField( max_length=30, label="Producto")
    descripcion = forms.CharField(max_length=150, label="Descripcion")
    precio = forms.IntegerField( label= "Precio")
    imagen = forms.ImageField(label= "Imagen", required=False)

    class Meta:
        model = Productos 
        fields = ['producto', 'descripcion', 'precio', 'imagen']
    

class SeguidoresFormulario(forms.Form):
    nombre = forms.CharField( max_length=30, label="Nombre")
    apellido = forms.CharField(max_length=30, label="Apellido")
    edad = forms.IntegerField( label= "Edad")
    email = forms.EmailField(label= "E-mail")

class ContactoFormulario(forms.ModelForm):
    nombre = models.CharField("Nombre", max_length=30)
    apellido = models.CharField("Apellido", max_length=30)
    email = models.EmailField("E-mail") 
    mensaje= models.TextField("Mensaje")   
    class Meta:
        model=Contacto
        fields= ['nombre', 'apellido', 'email', 'mensaje'] # o __all__

class UserRegisterForm(UserCreationForm):
        
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
        
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2' ]
            
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm): 
    #definimos lo básico para modificar del usuario

    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repita contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}