from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(label="Nombre de usuario", max_length=50, required=True)
    correo = forms.EmailField(label="Correo electrónico", max_length=100, required=True)
    edad = forms.IntegerField(label="Edad", required=True)

class ModeradorForm(forms.Form):
    nombre = forms.CharField(label="Nombre del moderador", max_length=50, required=True)
    correo = forms.EmailField(label="Correo electrónico", max_length=100, required=True)
    area_responsabilidad = forms.CharField(label="Área de responsabilidad", max_length=100, required=True)

class JuegoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del juego", max_length=50, required=True)
    genero = forms.CharField(label="Género del juego", max_length=50, required=True)
    plataforma = forms.CharField(label="Plataforma", max_length=50, required=True)