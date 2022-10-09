from django.test import TestCase

from reservations.models import Rental, Reservation


class RentalTests(TestCase):

	@classmethod
	def setUpTestData(cls):
		Rental.objects.create(name='Rental')

	def test_objects_quantity(self):
		rentals = Rental.objects.all()
		count = rentals.count()
		self.assertEqual(count, 1)

	def test_label_name(self):
		rental = Rental.objects.first()
		field_label = rental._meta.get_field('name').verbose_name
		self.assertEqual(field_label, 'Name')

	def test_max_length(self):
		rental = Rental.objects.first()
		max_length = rental._meta.get_field('name').max_length
		self.assertEqual(max_length, 125)

	def test_str(self):
		rental = Rental.objects.first()
		self.assertEqual(str(rental), 'Rental')


class ReservationTests(TestCase):

	@classmethod
	def setUpTestData(cls):
		r = Rental.objects.create(name='Rental')
		Reservation.objects.create(
			rental=r, checkin='2022-06-06', checkout='2022-06-10'
		)
		Reservation.objects.create(
			rental=r, checkin='2022-07-06', checkout='2022-07-10'
		)
		Reservation.objects.create(
			rental=r, checkin='2022-08-06', checkout='2022-08-10'
		)

	def test_objects_quantity(self):
		count = Reservation.objects.count()
		self.assertEqual(count, 3)

	def test_object_edit(self):
		obj = Reservation.objects.last()
		obj.checkin = '2033-01-01'
		obj.checkout = '2033-01-11'
		obj.save()
		self.assertEqual(str(obj.checkin), '2033-01-01')

	def test_object_delete(self):
		Reservation.objects.last().delete()
		count = Reservation.objects.count()
		self.assertEqual(count, 2)

	def test_label_name(self):
		reservation = Reservation.objects.first()
		field_label_rental = reservation._meta.get_field('rental').verbose_name
		field_label_checkin = reservation._meta.get_field('checkin').verbose_name
		field_label_checkout = reservation._meta.get_field('checkout').verbose_name
		self.assertEqual(field_label_rental, 'Rental')
		self.assertEqual(field_label_checkin, 'Check in date')
		self.assertEqual(field_label_checkout, 'Check out date')

	def test_str(self):
		reservation = Reservation.objects.first()
		self.assertEqual(str(reservation), 'Rental [2022-06-06 - 2022-06-10]')

	def test_get_prev_reservation_id(self):
		reservation = Reservation.objects.get(id=2)
		prev_id = reservation.get_prev_reservation_id()
		self.assertEqual(prev_id, 1)
