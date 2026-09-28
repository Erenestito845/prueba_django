from django.db import models

# Create your models here.
class CategoriaHardware(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Categoría")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría de Hardware"
        verbose_name_plural = "Categorías de Hardware"

class Componente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    marca = models.CharField(max_length=50, verbose_name="Marca")
    precio = models.PositiveIntegerField(verbose_name="Precio")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock")
    categoria = models.ForeignKey(CategoriaHardware, on_delete=models.CASCADE, verbose_name="Categoría")

    def __str__(self):
        return f"{self.marca} {self.nombre} - ${self.precio}"

    class Meta:
        verbose_name = "Componente"
        verbose_name_plural = "Componentes"