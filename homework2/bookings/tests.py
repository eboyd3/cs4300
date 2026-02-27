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
        
class MovieAPIIntegrationTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        self.movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date="2010-07-16",
            duration=148
        )

    def test_movie_list_returns_200(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_movie_list_returns_correct_data(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.data[0]['title'], "Inception")
        self.assertEqual(response.data[0]['duration'], 148)

    def test_movie_detail_returns_200(self):
        response = self.client.get(f'/api/movies/{self.movie.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_movie_detail_returns_correct_fields(self):
        response = self.client.get(f'/api/movies/{self.movie.id}/')
        self.assertIn('title', response.data)
        self.assertIn('description', response.data)
        self.assertIn('release_date', response.data)
        self.assertIn('duration', response.data)

    def test_movie_update(self):
        data = {
            "title": "Inception Updated",
            "description": "A mind-bending thriller",
            "release_date": "2010-07-16",
            "duration": 150
        }
        response = self.client.put(f'/api/movies/{self.movie.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['duration'], 150)

    def test_movie_delete(self):
        response = self.client.delete(f'/api/movies/{self.movie.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SeatAPIIntegrationTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        self.seat1 = Seat.objects.create(seat_number="A1", is_booked=False)
        self.seat2 = Seat.objects.create(seat_number="A2", is_booked=True)
        self.seat3 = Seat.objects.create(seat_number="A3", is_booked=False)

    def test_seat_list_returns_200(self):
        response = self.client.get('/api/seats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_seat_list_returns_all_seats(self):
        response = self.client.get('/api/seats/')
        self.assertEqual(len(response.data), 3)

    def test_seat_list_returns_correct_fields(self):
        response = self.client.get('/api/seats/')
        self.assertIn('seat_number', response.data[0])
        self.assertIn('is_booked', response.data[0])

    def test_available_seats_returns_200(self):
        response = self.client.get('/api/seats/available/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_available_seats_excludes_booked(self):
        response = self.client.get('/api/seats/available/')
        self.assertEqual(len(response.data), 2)
        for seat in response.data:
            self.assertFalse(seat['is_booked'])


class BookingAPIIntegrationTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.other_user = User.objects.create_user(username="otheruser", password="password")
        self.client.login(username="testuser", password="password")
        self.movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            release_date="2010-07-16",
            duration=148
        )
        self.seat = Seat.objects.create(seat_number="A1", is_booked=False)

    def test_create_booking_returns_201(self):
        data = {"movie": self.movie.id, "seat": self.seat.id}
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_booking_returns_correct_fields(self):
        data = {"movie": self.movie.id, "seat": self.seat.id}
        response = self.client.post('/api/bookings/', data)
        self.assertIn('movie', response.data)
        self.assertIn('seat', response.data)
        self.assertIn('booking_date', response.data)

    def test_create_booking_marks_seat_as_booked(self):
        data = {"movie": self.movie.id, "seat": self.seat.id}
        self.client.post('/api/bookings/', data)
        self.seat.refresh_from_db()
        self.assertTrue(self.seat.is_booked)

    def test_booking_list_only_shows_own_bookings(self):
        # Create a booking for other_user
        Booking.objects.create(movie=self.movie, seat=self.seat, user=self.other_user)
        seat2 = Seat.objects.create(seat_number="A2", is_booked=False)
        Booking.objects.create(movie=self.movie, seat=seat2, user=self.user)

        response = self.client.get('/api/bookings/')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user'], self.user.id)

    def test_unauthenticated_returns_403(self):
        self.client.logout()
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
