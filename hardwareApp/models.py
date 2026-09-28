from django.db import models

# Guarda las categorías disponibles para clasificar los componentes.
class CategoriaHardware(models.Model):
    # Nombre que identifica y se muestra para esta categoría.
    nombre = models.CharField(max_length=100, verbose_name="Categoría")

    def __str__(self):
        # Muestra el nombre en el panel de administración y otros listados.
        return self.nombre

    class Meta:
        # Define las etiquetas legibles usadas por Django.
        verbose_name = "Categoría de Hardware"
        verbose_name_plural = "Categorías de Hardware"

# Guarda los datos de cada componente del catálogo.
class Componente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    marca = models.CharField(max_length=50, verbose_name="Marca")
    precio = models.PositiveIntegerField(verbose_name="Precio")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock")
    # Si se elimina una categoría, también se eliminan sus componentes asociados.
    categoria = models.ForeignKey(CategoriaHardware, on_delete=models.CASCADE, verbose_name="Categoría")

    def __str__(self):
        # Resume el componente con su marca, nombre y precio.
        return f"{self.marca} {self.nombre} - ${self.precio}"

    class Meta:
        # Define las etiquetas legibles usadas por Django.
        verbose_name = "Componente"
        verbose_name_plural = "Componentes"