from django.db import models


class Rental(models.Model):
	name = models.CharField(max_length=125, verbose_name="Name")
	
	class Meta:
		ordering = ['name']
		verbose_name = "Rental"
		verbose_name_plural = "Rentals"
		
	def __str__(self):
		return self.name
	

class Reservation(models.Model):
	rental = models.ForeignKey(
		Rental, on_delete=models.CASCADE, verbose_name="Rental"
	)
	checkin = models.DateField(verbose_name="Check in date")
	checkout = models.DateField(verbose_name="Check out date")

	def get_prev_reservation_id(self):
		last_reservation = Reservation.objects.filter(
			rental=self.rental, id__lt=self.id
		).last()
		if last_reservation is None:
			return "-"
		return last_reservation.id

	class Meta:
		ordering = ['id']
		verbose_name = "Reservation"
		verbose_name_plural = "Reservations"

	def __str__(self):
		return f"{self.rental.name} [{self.checkin} - {self.checkout}]"
