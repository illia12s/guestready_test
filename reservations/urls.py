from django.urls import path
from reservations import views


urlpatterns = [
    path("", views.ReservationView.as_view(), name='list-reservations'),
]

