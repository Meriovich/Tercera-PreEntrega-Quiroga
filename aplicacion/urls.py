from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),
    path('usuarios', usuarios, name="usuarios"),
    path('staff', staff, name="staff"),
    path('actividades', actividades, name="actividades"),

    path('actividad_form/', actividadForm, name="actividad_form"),
    path('actividad_form2/', ActividadForm2, name="actividad_form2"),

    path('buscar_comision/', buscarComision, name="buscar_comision"),   
    path('buscar2/', buscar2, name="buscar2"),

    path('buscarStaff/', buscarStaff, name="buscarStaff"), 
    path('buscarUsuario/', buscarUsuario, name="buscarUsuario"), 
]