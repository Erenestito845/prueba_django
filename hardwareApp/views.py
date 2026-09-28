"""Vistas del catálogo de componentes de hardware."""


import os

from django.shortcuts import render
from django.conf import settings
from .models import Componente

def inicio_hardware(request):
    """Renderiza la página principal del catálogo de hardware."""
    return render(request, 'hadwareApp/inicio.html')


def lista_hardware(request):
    # Obtiene todos los componentes guardados en la base de datos.
    componentes = Componente.objects.all()
    # Envía la lista a la plantilla con la clave que esta espera.
    return render(request, 'hadwareApp/lista.html', {'componentes': componentes})