from django.contrib import admin
from .models import *
# Registrar modelos aquí

"""" <--- Registro de modelos de ESTUDIANTES ---> """
admin.site.register(Estudiante)
admin.site.register(ServicioSocial)
admin.site.register(PracticaProf)
admin.site.register(Taller)
admin.site.register(VinculacionAcad)
admin.site.register(Egresado)