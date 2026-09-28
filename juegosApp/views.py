"""Vistas del catálogo de juegos."""

from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import JuegoForm
from .models import Juego


def inicio(request):
    """Renderiza la página principal del catálogo de juegos."""
    return render(request, 'juegosApp/inicio.html')


def lista_juegos(request):
    query = request.GET.get('q', '').strip()
    juegos = Juego.objects.all()
    if query:
        juegos = juegos.filter(Q(titulo__icontains=query) | Q(genero__icontains=query))
    return render(request, 'juegosApp/lista.html', {'juegos': juegos, 'query': query})


def agregar_juego(request):
    form = JuegoForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('juegos_lista')
    return render(request, 'juegosApp/form_juego.html', {'form': form, 'accion': 'Agregar'})


def editar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    form = JuegoForm(request.POST if request.method == 'POST' else None, instance=juego)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('juegos_lista')
    return render(
        request,
        'juegosApp/form_juego.html',
        {'form': form, 'accion': 'Modificar', 'juego': juego},
    )


@require_POST
def eliminar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    juego.delete()
    return redirect('juegos_lista')