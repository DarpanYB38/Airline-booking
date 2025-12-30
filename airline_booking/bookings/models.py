from django.db import models

# Create your models here.
class Flight(models.Model):
    Flight_number = models.CharField(max_length=20)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.Flight_number} ({self.origin} {self.destination})"
    
class Seat(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)
    is_available = models.CharField(default=True)

    def __str__(self):
        return self.seat_number
    
class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Confirmed")

    def __str__(self):
        return f"Booking {self.id} - {self.status}"
    
