from django.shortcuts import render, get_object_or_404
from bookings.models import *

# Create your views here.
def flight_search(request):
    flights = Flight.objects.all()
    return render(request,'flight_search.html',{'flights': flights})

def seat_selection(request, flight_id):
    flight = get_object_or_404(Flight, id= flight_id)
    seats = Seat.objects.filter(flight=flight).order_by('seat_number')
    return render(request, 'seat_selection.html',{'flight': flight, 'seats': seats})

def booking_confirmation(request, seat_id):
    seat = get_object_or_404(Seat, id=seat_id)
    seat.is_avaliable = False
    seat.save()
    booking = Booking.objects.create(flight=seat.flight, seat=seat)
    return render(request,'booking_confirmed.html',{'booking': booking})

def flight_search(request):
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')

    flights = Flight.objects.all()

    if origin:
        flights = flights.filter(origin__icontains=origin)
    if destination:
        flights = flights.filter(destination__icontains=destination)

    return render(request, 'flight_search.html', {
        'flights': flights,
        'origin': origin,
        'destination': destination
    })

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Make seat available again
    booking.seat.is_available = True
    booking.seat.save()

    # Update booking status
    booking.status = "Cancelled"
    booking.save()

    return render(request, 'cancel_booking.html', {'booking': booking})
