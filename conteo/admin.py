from django.contrib import admin
from .models import Paciente, Entidad, Municipio

# Register your models here.
admin.site.register(Paciente)

admin.site.register(Entidad)

admin.site.register(Municipio)
