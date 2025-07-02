from django.contrib import admin
from usuarios.models import *


# Register your models here.

class UsuariosAdmin(admin.ModelAdmin):
    ...

class CarrosAdmin(admin.ModelAdmin):
    ...

class EstacionamentosAdmin(admin.ModelAdmin):
    ...

admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(Carros, CarrosAdmin)
admin.site.register(Estacionamentos, EstacionamentosAdmin)