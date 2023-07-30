from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),
    path('usuarios', usuarios, name="usuarios"),
    path('staff', staff, name="staff"),
    path('actividades', actividades, name="actividades"),
]