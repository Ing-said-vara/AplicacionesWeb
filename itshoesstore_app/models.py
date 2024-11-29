from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)  
    descripcion = models.TextField()             
    precio = models.DecimalField(max_digits=10, decimal_places=2)  
    stock = models.IntegerField()               
    fecha_agregado = models.DateTimeField(auto_now_add=True) 

    def __str__(self):

        return self.nombre

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    telefono = models.CharField(max_length=15, null=True, blank=True)  
    direccion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username