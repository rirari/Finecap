from django.contrib import admin

from stand.models import Stand, Empresa, Reserva

# Register your models here.


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria")

@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    list_display = ("localizacao", "valor")