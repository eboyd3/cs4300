from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie, Seat, Booking
from django.utils import timezone

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie",
            release_date="2024-01-01",
            duration=120
        )

    def test_movie_created(self):
        self.assertEqual(self.movie.title, "Test Movie")

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Test Movie")


class SeatModelTest(TestCase):
    def setUp(self):
        self.seat = Seat.objects.create(
            seat_number="A1",
            is_booked=False
        )

    def test_seat_created(self):
        self.assertEqual(self.seat.seat_number, "A1")

    def test_seat_default_not_booked(self):
        self.assertFalse(self.seat.is_booked)

    def test_seat_str(self):
        self.assertEqual(str(self.seat), "A1")


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie",
            release_date="2024-01-01",
            duration=120
        )
        self.seat = Seat.objects.create(seat_number="A1", is_booked=False)
        self.booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )

    def test_booking_created(self):
        self.assertEqual(self.booking.movie.title, "Test Movie")
        self.assertEqual(self.booking.seat.seat_number, "A1")
        self.assertEqual(self.booking.user.username, "testuser")


class MovieAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie",
            release_date="2024-01-01",
            duration=120
        )

    def test_get_movies(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_movie(self):
        data = {
            "title": "New Movie",
            "description": "A new movie",
            "release_date": "2024-06-01",
            "duration": 90
        }
        response = self.client.post('/api/movies/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class SeatAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        self.seat = Seat.objects.create(seat_number="A1", is_booked=False)
        Seat.objects.create(seat_number="A2", is_booked=True)

    def test_get_seats(self):
        response = self.client.get('/api/seats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_available_seats(self):
        response = self.client.get('/api/seats/available/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # only A1 is available


class BookingAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie",
            release_date="2024-01-01",
            duration=120
        )
        self.seat = Seat.objects.create(seat_number="A1", is_booked=False)

    def test_create_booking(self):
        data = {
            "movie": self.movie.id,
            "seat": self.seat.id,
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_bookings(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_cannot_book(self):
        self.client.logout()
        data = {"movie": self.movie.id, "seat": self.seat.id}
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)