"""Vistas del catálogo de juegos."""

import json
import os

from django.shortcuts import render
from django.conf import settings


def inicio(request):
    """Renderiza la página principal del catálogo de juegos."""
    return render(request, 'juegosApp/inicio.html')


def lista_juegos(request):
    """Lee los juegos desde JSON y los envía a la plantilla del catálogo."""
    # BASE_DIR permite construir la ruta sin depender de la carpeta actual.
    ruta_json = os.path.join(settings.BASE_DIR, 'data', 'juegos.json')
    # El archivo JSON funciona como fuente de datos del catálogo.
    with open(ruta_json, 'r', encoding='utf-8') as file:
        datos = json.load(file)
    # La clave 'juegos' es el nombre que utilizará la plantilla HTML.
    return render(request, 'juegosApp/lista.html', {'juegos': datos})