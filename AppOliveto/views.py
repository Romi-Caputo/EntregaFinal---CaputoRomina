from cgitb import html
from http.client import PRECONDITION_FAILED
from tkinter import image_names
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Avatar, Contacto, Productos, Seguidores
from .forms import ProductosFormulario, SeguidoresFormulario, ContactoFormulario, UserEditForm, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# @login_required
def inicio(request):
      avatares = Avatar.objects.filter(user=request.user.id)
      return render(request, "AppOliveto/inicio.html" ,{"url": avatares[0].imagen.url} )
      
    
def login_request(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("Inicio")
            else:
                return redirect("Login")
        else:
            return redirect("Login")
            
    form = AuthenticationForm()
    
    return render(request, "AppOliveto/login.html", {"form":form})

def register(request):
      
      if request.method == "POST":

            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                 
                  form.save()

                  return render(request, "AppOliveto/inicio.html", {"mensaje": "usuario creado"})

      else: 
            form = UserRegisterForm()

      return render(request, "AppOliveto/register.html", {"form": form})

@login_required
def about(request):
    return render(request, "AppOliveto/about.html") 

@login_required
def productos(request):
      productos = Productos.objects.all()
      contexto={"productos": productos}
      return render(request, "AppOliveto/productos.html",contexto)

@staff_member_required
def crear_productos(request):
    # post
    if request.method == "POST":
        
        formulario = ProductosFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            productos = Productos(producto=info["producto"],descripcion=info["descripcion"],precio=info["precio"],imagen=info["imagen"])
            productos.save()

            return redirect("Productos")

        return render(request,"AppOliveto/inicio.html",{"form":formulario})

    # get
    formulariovacio = ProductosFormulario()
    return render(request,"AppOliveto/productos_formulario.html",{"form":formulariovacio})

@staff_member_required
def eliminarProducto(request, producto_id):

    productos = Productos.objects.get(id=producto_id)
    productos.delete()
    
    return redirect("Productos")
@staff_member_required
def editarProducto(request, producto_id):

    productos = Productos.objects.get(id=producto_id)
    if request.method == "POST":
    
        formulario = ProductosFormulario(request.POST, request.FILES or None, producto_id)
        if formulario.is_valid():
            info_producto = formulario.cleaned_data
            productos.producto = info_producto["producto"]
            productos.descripcion = info_producto["descripcion"]
            productos.precio = info_producto["precio"]
            
            if request.FILES:
                
                productos.imagen = request.FILES["imagen"]
            productos.save()
            return redirect ("Productos")
    
     #get
    formulario_vacio = ProductosFormulario(initial={
            "producto":productos.producto,
            "descripcion": productos.descripcion,
            "precio": productos.precio,
            "imagen": productos.imagen})
    

    return render(request, "AppOliveto/editar_productos.html", {"form":formulario_vacio})    

@login_required       
def seguidores(request):

      seguidores = Seguidores.objects.all()
      contexto={"seguidores": seguidores}
      return render(request, "AppOliveto/seguidores.html",contexto)

@login_required
def crear_seguidores(request):
    # post
    if request.method == "POST":
        
        formulario = SeguidoresFormulario(request.POST)

        if formulario.is_valid():
            
            info_seg= formulario.cleaned_data

            seguidores= Seguidores(nombre=info_seg["nombre"], apellido=info_seg["apellido"], edad=info_seg["edad"], email=info_seg["email"] )
            seguidores.save()
            return redirect("Seguidores")

        return render(request,"AppOliveto/inicio.html",{"form":formulario})

    # get
    formulariovacio = SeguidoresFormulario()
    return render(request,"AppOliveto/seguidores_formulario.html",{"form":formulariovacio})

@login_required
def contacto(request):

    # post
    if request.method == "POST":
        
        formulario = ContactoFormulario(request.POST)

        if formulario.is_valid():
            
            info_cont= formulario.cleaned_data

            contactos= Contacto(nombre=info_cont["nombre"], apellido=info_cont["apellido"], mensaje=info_cont["mensaje"], email=info_cont["email"] )
            contactos.save()
        return render(request,"AppOliveto/ok_enviocontacto.html",{"form":formulario})

    # get
    formulariovacio = ContactoFormulario()
    return render(request,"AppOliveto/contacto_formulario.html",{"form":formulariovacio}) 

@login_required
def editarPerfil(request):
      #se instancia el Login; 
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid(): 
                  informacion = miFormulario.cleaned_data
                  
                  #datos que modificaríamos
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "AppOliveto/inicio.html") #

      else:
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      return render(request, "AppOliveto/editarperfil.html", {"miFormulario": miFormulario, "usuario": usuario})

