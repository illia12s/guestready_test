from django.test import TestCase
from django.urls import reverse

from reservations.models import Rental, Reservation
from reservations.views import ReservationView


class ReservationViewTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		rental_1 = Rental.objects.create(name='Rental_1')
		rental_2 = Rental.objects.create(name='Rental_2')
		Reservation.objects.create(
			rental=rental_1, checkin='2022-04-01', checkout='2022-04-12'
		)
		Reservation.objects.create(
			rental=rental_1, checkin='2022-04-15', checkout='2022-04-22'
		)
		Reservation.objects.create(
			rental=rental_1, checkin='2022-05-01', checkout='2022-05-10'
		)
		Reservation.objects.create(
			rental=rental_2, checkin='2022-04-01', checkout='2022-04-12'
		)
		Reservation.objects.create(
			rental=rental_2, checkin='2022-04-15', checkout='2022-04-30'
		)
		Reservation.objects.create(
			rental=rental_2, checkin='2022-05-01', checkout='2022-05-10'
		)

	def test_view_url(self):
		response = self.client.get('')
		self.assertEqual(response.status_code, 200)

	def test_template(self):
		response = self.client.get('')
		self.assertTemplateUsed(response, 'reservations/reservation_list.html')

	def test_view_reverse(self):
		response = self.client.get(reverse('list-reservations'))
		self.assertEqual(response.status_code, 200)
