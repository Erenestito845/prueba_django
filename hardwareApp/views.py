"""Vistas del catálogo de componentes de hardware."""

from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ComponenteForm
from .models import Componente


def inicio_hardware(request):
    """Renderiza la página principal del catálogo de hardware."""
    return render(request, 'hadwareApp/inicio.html')


def lista_hardware(request):
    query = request.GET.get('q', '').strip()
    componentes = Componente.objects.select_related('categoria').all()
    if query:
        componentes = componentes.filter(
            Q(nombre__icontains=query)
            | Q(marca__icontains=query)
            | Q(categoria__nombre__icontains=query)
        )
    return render(
        request,
        'hadwareApp/lista.html',
        {'componentes': componentes, 'query': query},
    )


def agregar_componente(request):
    form = ComponenteForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('hardware_lista')
    return render(
        request,
        'hadwareApp/form_componente.html',
        {'form': form, 'accion': 'Agregar'},
    )


def editar_componente(request, id):
    componente = get_object_or_404(Componente, id=id)
    form = ComponenteForm(
        request.POST if request.method == 'POST' else None,
        instance=componente,
    )
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('hardware_lista')
    return render(
        request,
        'hadwareApp/form_componente.html',
        {'form': form, 'accion': 'Modificar', 'componente': componente},
    )


@require_POST
def eliminar_componente(request, id):
    componente = get_object_or_404(Componente, id=id)
    componente.delete()
    return redirect('hardware_lista')

