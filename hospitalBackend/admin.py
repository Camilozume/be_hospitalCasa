from django.contrib import admin
from .models.usuario import Usuario
from .models.medico import Medico
from .models.paciente import Paciente

admin.site.register(Usuario)
admin.site.register(Medico)
admin.site.register(Paciente)

# Register your models here.
