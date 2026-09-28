from django.test import TestCase
from django.urls import reverse

from .models import CategoriaHardware, Componente


class ComponenteCrudTests(TestCase):
	def setUp(self):
		self.categoria = CategoriaHardware.objects.create(nombre='Tarjetas gráficas')
		self.componente = Componente.objects.create(
			nombre='RTX 5090',
			marca='NVIDIA',
			precio=1000000,
			stock=2,
			categoria=self.categoria,
		)

	def test_buscar_por_nombre_marca_o_categoria(self):
		response = self.client.get(reverse('hardware_lista'), {'q': 'nvidia'})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'RTX 5090')

	def test_agregar_componente(self):
		response = self.client.post(reverse('hardware_componente_agregar'), {
			'nombre': 'RX 9070',
			'marca': 'AMD',
			'precio': 500000,
			'stock': 4,
			'categoria': self.categoria.id,
		})

		self.assertRedirects(response, reverse('hardware_lista'))
		self.assertTrue(Componente.objects.filter(nombre='RX 9070').exists())

	def test_editar_componente(self):
		response = self.client.post(
			reverse('hardware_componente_editar', args=[self.componente.id]),
			{
				'nombre': 'RTX 5090 actualizada',
				'marca': self.componente.marca,
				'precio': self.componente.precio,
				'stock': self.componente.stock,
				'categoria': self.categoria.id,
			},
		)

		self.assertRedirects(response, reverse('hardware_lista'))
		self.componente.refresh_from_db()
		self.assertEqual(self.componente.nombre, 'RTX 5090 actualizada')

	def test_eliminar_componente_por_post(self):
		response = self.client.post(
			reverse('hardware_componente_eliminar', args=[self.componente.id])
		)

		self.assertRedirects(response, reverse('hardware_lista'))
		self.assertFalse(Componente.objects.filter(id=self.componente.id).exists())

	def test_eliminar_componente_no_acepta_get(self):
		response = self.client.get(
			reverse('hardware_componente_eliminar', args=[self.componente.id])
		)

		self.assertEqual(response.status_code, 405)
		self.assertTrue(Componente.objects.filter(id=self.componente.id).exists())
