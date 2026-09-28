from django.db import models

# Create your models here.
class Plataforma(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Plataforma") # Ej: PC, PS5, Switch

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    genero = models.CharField(max_length=50, verbose_name="Género")
    precio = models.PositiveIntegerField(verbose_name="Precio")
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE, verbose_name="Plataforma")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"