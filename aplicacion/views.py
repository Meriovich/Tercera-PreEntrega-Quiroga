from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def usuarios(request):
    return render(request, "aplicacion/usuarios.html")

def actividades(request):
    ctx = {"actividades": Actividad.objects.all()}
    return render(request, "aplicacion/actividades.html", ctx)

def profesores(request):
    return render(request, "aplicacion/profesores.html")