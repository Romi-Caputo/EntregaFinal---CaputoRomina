from django.urls import path
from AppOliveto import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
path("inicio/", views.inicio, name="Inicio"),
path("sobremi", views.about, name="Acercademi"),
path('login', views.login_request, name='Login'),
path('logout', LogoutView.as_view(template_name='AppOliveto/logout.html'), name='logout'),
path('register/', views.register, name="register"),
path('editarperfil', views.editarPerfil, name='EditarPerfil'),
path("productos", views.productos, name="Productos"),
path("crearproductos", views.crear_productos, name= "CrearProductos"),
path("eliminarproductos/<producto_id>/", views.eliminarProducto, name="EliminarProductos"),
path("editarproductos/<producto_id>/", views.editarProducto, name="EditarProductos"),
path("seguidores", views.seguidores, name="Seguidores"),
path("crearseguidores", views.crear_seguidores, name="CrearSeguidores"),
path("contacto", views.contacto, name="Contacto"),

]