from django.db import models
from django.contrib.auth.models import User

class Productos(models.Model):
    producto = models.CharField("Producto", max_length=30)
    descripcion = models.CharField("Descripcion Producto", max_length=150)
    precio = models.FloatField("Precio $")
    imagen = models.ImageField("Imagen", upload_to="productos", null=True, blank=True) 

    def __str__(self):
        return f"Productos: {self.producto} - Descripción: {self.descripcion} "

class Seguidores(models.Model):
    nombre = models.CharField("Nombre Seguidor", max_length=30)
    apellido = models.CharField("Apellido Seguidor", max_length=30)
    edad = models.SmallIntegerField("Edad")
    email = models.EmailField("E-mail")

class Contacto(models.Model):
    nombre = models.CharField("Nombre", max_length=30)
    apellido = models.CharField("Apellido", max_length=30)
    email = models.EmailField("E-mail") 
    mensaje= models.TextField("Mensaje")

    def __str__(self):
        return self.nombre
    
class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatar', null=True, blank = True)






# Create your models here.
