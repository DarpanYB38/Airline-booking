from django.contrib import admin
from bookings.models import *

# Register your models here.
admin.site.register(Flight)
admin.site.register(Seat)
admin.site.register(Booking)
