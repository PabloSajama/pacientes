# Create your models here.
from django.db import models # type: ignore

class pacie(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    email = models.CharField (max_length=100)
    direccion = models.TextField(max_length=200)
    telefono = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nombre
