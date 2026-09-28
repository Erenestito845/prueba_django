from django.contrib import admin
from .models import Plataforma, Juego
# Register your models here.
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'precio', 'plataforma')
    search_fields = ('titulo', 'genero')
    list_filter = ('plataforma', 'genero')

admin.site.register(Plataforma)
admin.site.register(Juego, JuegoAdmin)