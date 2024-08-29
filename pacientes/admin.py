from django.contrib import admin # type: ignore
from .models import pacie

@admin.register(pacie)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'direccion')