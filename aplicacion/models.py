from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    edad = models.IntegerField()

class Moderador(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    area_responsabilidad = models.CharField(max_length=100)

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)

from django import forms

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'edad']

class ModeradorForm(forms.ModelForm):
    class Meta:
        model = Moderador
        fields = ['nombre', 'correo', 'area_responsabilidad']

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['nombre', 'genero', 'plataforma']