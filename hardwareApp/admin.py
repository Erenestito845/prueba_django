"""Configuración de los modelos de hardware para el panel de administración."""

from django.contrib import admin
from .models import CategoriaHardware, Componente
 
class ComponenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'marca', 'precio', 'stock', 'categoria')
    search_fields = ('nombre', 'marca')
    list_filter = ('categoria', 'marca')

admin.site.register(CategoriaHardware)
admin.site.register(Componente, ComponenteAdmin)
