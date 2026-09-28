"""Vistas del catálogo de componentes de hardware."""

import json
import os

from django.shortcuts import render
from django.conf import settings


def inicio_hardware(request):
    """Renderiza la página principal del catálogo de hardware."""
    return render(request, 'hadwareApp/inicio.html')


def lista_hardware(request):
    """Lee los componentes desde JSON y los envía a la plantilla del catálogo."""
    # BASE_DIR permite localizar el JSON desde cualquier directorio de ejecución.
    ruta_json = os.path.join(settings.BASE_DIR, 'data', 'hardware.json')
    # Se cargan todos los componentes para entregarlos a la plantilla.
    with open(ruta_json, 'r', encoding='utf-8') as file:
        datos = json.load(file)
    # La plantilla espera los datos bajo el nombre 'componentes'.
    return render(request, 'hadwareApp/lista.html', {'componentes': datos})