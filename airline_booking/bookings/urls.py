from django.contrib import admin
from django.urls import path
from bookings.views import *

urlpatterns = [
    path('',flight_search,name='flight_search'),
    path('flight/<int:flight_id>/',seat_selection,name='seat_selection'),
    path('book/<int:seat_id>/',booking_confirmation, name='booking_confirmation'),
    path('cancle/<int:booking_id>/',cancel_booking, name='cancel_booking'),
]