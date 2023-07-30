from django.contrib import admin
from .models import Actividad, Usuario, Staff

# Register your models here.
admin.site.register(Actividad)
admin.site.register(Usuario)
admin.site.register(Staff)