"""Vistas del catálogo de juegos."""

import json
import os

from django.shortcuts import render
from django.conf import settings
from .models import Juego

def inicio(request):
    """Renderiza la página principal del catálogo de juegos."""
    return render(request, 'juegosApp/inicio.html')

def lista_juegos(request):
    # Obtiene todos los juegos guardados en la base de datos.
    juegos = Juego.objects.all()
    # Envía los juegos a la plantilla con la clave que esta espera.
    return render(request, 'juegosApp/lista.html', {'juegos': juegos})