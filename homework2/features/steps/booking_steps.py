from behave import given, when, then
from django.contrib.auth.models import User
from bookings.models import Movie, Seat, Booking
import json

@given('the database has movies')
def step_create_movies(context):
    context.movie = Movie.objects.create(
        title="Inception",
        description="A mind-bending thriller",
        release_date="2010-07-16",
        duration=148
    )

@given('the database has seats')
def step_create_seats(context):
    context.seat = Seat.objects.create(seat_number="A1", is_booked=False)
    Seat.objects.create(seat_number="A2", is_booked=True)

@given('I am logged in as a user')
def step_login(context):
    context.user = User.objects.create_user(username="testuser", password="password")
    context.client.login(username="testuser", password="password")

@given('I am not logged in')
def step_not_logged_in(context):
    context.client.logout()

@given('another user has a booking')
def step_other_user_booking(context):
    other_user = User.objects.create_user(username="otheruser", password="password")
    movie = Movie.objects.create(
        title="Other Movie",
        description="Another movie",
        release_date="2024-01-01",
        duration=90
    )
    seat = Seat.objects.create(seat_number="B1", is_booked=True)
    Booking.objects.create(movie=movie, seat=seat, user=other_user)

@when('I request the list of movies')
def step_get_movies(context):
    context.response = context.client.get('/api/movies/')

@when('I request available seats')
def step_get_available_seats(context):
    context.response = context.client.get('/api/seats/available/')

@when('I create a booking')
def step_create_booking(context):
    data = {
        "movie": context.movie.id,
        "seat": context.seat.id,
    }
    context.response = context.client.post(
        '/api/bookings/',
        json.dumps(data),
        content_type='application/json'
    )

@when('I request my booking history')
def step_get_bookings(context):
    context.response = context.client.get('/api/bookings/')

@then('I should receive a {status_code:d} status code')
def step_check_status(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, got {context.response.status_code}"

@then('the response should contain a list of movies')
def step_check_movies(context):
    data = json.loads(context.response.content)
    assert isinstance(data, list), "Response is not a list"
    assert len(data) > 0, "Movie list is empty"

@then('the response should only contain unbooked seats')
def step_check_available_seats(context):
    data = json.loads(context.response.content)
    for seat in data:
        assert seat['is_booked'] == False, f"Seat {seat['seat_number']} is booked"

@then('the seat should be marked as booked')
def step_check_seat_booked(context):
    context.seat.refresh_from_db()
    assert context.seat.is_booked == True, "Seat was not marked as booked"

@then('I should only see my own bookings')
def step_check_own_bookings(context):
    data = json.loads(context.response.content)
    for booking in data:
        assert booking['user'] == context.user.id, "Booking belongs to another user"
