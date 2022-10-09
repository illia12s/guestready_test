from django.views.generic.list import ListView

from reservations.models import Reservation


class ReservationView(ListView):
	model = Reservation

