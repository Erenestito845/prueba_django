"""Rutas principales del proyecto y punto de entrada de las aplicaciones."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de administración incluido por Django.
    path('admin/', admin.site.urls),
    # El catálogo de juegos utiliza la raíz del sitio.
    path('', include('juegosApp.urls')),
    # Todas las rutas de hardware quedan agrupadas bajo /hard/.
    path('hard/', include('hardwareApp.urls'))
]
