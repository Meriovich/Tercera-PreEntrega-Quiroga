from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def usuarios(request):
    return render(request, "aplicacion/usuarios.html")

def actividades(request):
    ctx = {"actividades": Actividad.objects.all()}
    return render(request, "aplicacion/actividades.html", ctx)

def actividadForm(request):
    if request.method == "POST":
        actividad = Actividad(nombre=request.POST['nombre'], comision=request.POST['comision'])
        actividad.save()
        return HttpResponse("Se aplicó la solicitud exitosamente!")
    return render(request, "aplicacion/actividadForm.html")

def ActividadForm2(request):
    if request.method == "POST":
        miForm = ActivdadForm(request.POST)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            actividad = Actividad(nombre=informacion['nombre'], comision=informacion['comision'])
            actividad.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = ActivdadForm()

    return render(request, "aplicacion/actividadForm2.html", {"form":miForm})

def staff(request):
    return render(request, "aplicacion/staff.html")

def buscarComision(request):
    return render(request, "aplicacion/buscarComision.html")

def buscar2(request):
    if request.GET['comision']:
        comision = request.GET['comision']
        actividades = Actividad.objects.filter(comision__icontains=comision)
        return render(request, 
                      "aplicacion/resultadosComision.html",
                      {"comision": comision, "actividades":actividades})
    return HttpResponse("No se ingresaron datos para buscar")

def buscarStaff(request):
    if 'staff' in request.GET:
        staff_query = request.GET['staff']
        resultados_staff = Staff.objects.filter(apellido__icontains=staff_query)
        return render(request, "aplicacion/resultados_staff.html", {
            "staff_query": staff_query,
            "resultados_staff": resultados_staff,
        })
    return HttpResponse("No se ingresaron datos para buscar")

def buscarUsuario(request):
    if 'usuario' in request.GET:
        usuario_query = request.GET['usuario']
        resultados_usuarios = Usuario.objects.filter(apellido__icontains=usuario_query)

        return render(request, "aplicacion/resultados_usuarios.html", {
            "usuario_query": usuario_query,
            "resultados_usuarios": resultados_usuarios,
        })

    return HttpResponse("No se ingresaron datos para buscar")