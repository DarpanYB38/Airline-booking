# Airline Seat Booking System (MVP)

## Overview
This is a Django-based MVP airline seat booking platform built from a Product Requirements Document (PRD).  
The goal is to demonstrate core booking flows, seat inventory management, and scalable architecture.

## Features
- Flight search by origin and destination
- Airline-style seat selection (available / unavailable)
- Booking creation and confirmation
- Booking cancellation with seat release
- Admin dashboard for managing flights and seats

## Tech Stack
- Backend: Django
- Frontend: Django Templates (HTML, CSS)
- Database: SQLite (MVP)
- Styling: Custom CSS

## Booking Flow
1. User searches flights
2. Selects a flight and seat
3. Booking is created and seat is locked
4. User can cancel booking and seat becomes available

## MVP Scope
- No real payment gateway (sandbox-ready)
- No airline API integration
- Focus on clean logic and extensibility

## Future Enhancements
- Business & economy seat classes
- Payment integration (Stripe)
- Authentication & user profiles
- Real airline data integrations

## Setup
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
