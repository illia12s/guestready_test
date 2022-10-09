from django.contrib import admin

from .models import Rental, Reservation


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', )
	search_fields = ['name']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	list_display = ('id', 'rent_name', 'checkin', 'checkout', )
	list_filter = ('checkin', 'checkout', )

	@admin.display(description='Rental')
	def rent_name(self, obj):
		return obj.rental.name
