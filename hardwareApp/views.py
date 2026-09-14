import json, os
from django.shortcuts import render
from django.conf import settings
# Create your views here.
def inicio_hardware(request):
    return render(request, 'hadwareApp/inicio.html')

def lista_hardware(request):
    ruta_json = os.path.join(settings.BASE_DIR, 'data', 'hardware.json')
    with open(ruta_json, 'r', encoding='utf-8') as file:
        datos = json.load(file)
    return render(request, 'hadwareApp/lista.html', {'componentes': datos})