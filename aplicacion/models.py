from django.db import models

# Create your models here.
class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Staff(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"