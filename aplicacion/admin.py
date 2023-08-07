from django.contrib import admin
from .models import Usuario, Moderador, Juego

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'edad')

@admin.register(Moderador)
class ModeradorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'area_responsabilidad')

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero', 'plataforma')