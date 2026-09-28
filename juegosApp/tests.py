from django.test import TestCase
from django.urls import reverse

from .models import Juego, Plataforma


class JuegoCrudTests(TestCase):
	def setUp(self):
		self.plataforma = Plataforma.objects.create(nombre='PC')
		self.juego = Juego.objects.create(
			titulo='Aventura inicial',
			genero='Aventura',
			precio=10000,
			plataforma=self.plataforma,
		)

	def test_buscar_por_titulo_o_genero(self):
		response = self.client.get(reverse('juegos_lista'), {'q': 'aventura'})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Aventura inicial')

	def test_agregar_juego(self):
		response = self.client.post(reverse('juego_agregar'), {
			'titulo': 'Juego nuevo',
			'genero': 'Acción',
			'precio': 25000,
			'plataforma': self.plataforma.id,
		})

		self.assertRedirects(response, reverse('juegos_lista'))
		self.assertTrue(Juego.objects.filter(titulo='Juego nuevo').exists())

	def test_editar_juego(self):
		response = self.client.post(reverse('juego_editar', args=[self.juego.id]), {
			'titulo': 'Título actualizado',
			'genero': self.juego.genero,
			'precio': self.juego.precio,
			'plataforma': self.plataforma.id,
		})

		self.assertRedirects(response, reverse('juegos_lista'))
		self.juego.refresh_from_db()
		self.assertEqual(self.juego.titulo, 'Título actualizado')

	def test_eliminar_juego_por_post(self):
		response = self.client.post(reverse('juego_eliminar', args=[self.juego.id]))

		self.assertRedirects(response, reverse('juegos_lista'))
		self.assertFalse(Juego.objects.filter(id=self.juego.id).exists())

	def test_eliminar_juego_no_acepta_get(self):
		response = self.client.get(reverse('juego_eliminar', args=[self.juego.id]))

		self.assertEqual(response.status_code, 405)
		self.assertTrue(Juego.objects.filter(id=self.juego.id).exists())
