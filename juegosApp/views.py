from django.shortcuts import render
#esto sirve para renderisar html
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def inicio(request):
    return render(request, 'juegos/inicio.html')

def lista_juegos(request):
    ruta_json = os.path.join(settings.BASE_DIR, 'data', 'juegos.json')
    # Abre y lee el archivo
    with open(ruta_json, 'r', encoding='utf-8') as file:
        datos = json.load(file)
    return render(request, 'juegos/lista.html', {'juegos': datos})