Movie Theater Booking System
A RESTful API built with Django and Django REST Framework for managing movie bookings.
Website link:
https://cs4300-sytx.onrender.com/api/
Go to the other API endpoints (listed below) to see more

Local Setup

Prerequisites:
Python 3.12+
Git

Installation:

Clone the repository:
   git clone git@github.com:yourusername/your-repo.git
   cd your-repo/homework2

Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate

Install dependencies:
   pip install -r requirements.txt

Apply migrations:
   python manage.py migrate

Run the development server:
   python manage.py runserver 0.0.0.0:3000

Visit the API at http://localhost:3000/api/

Project Structure:
homework2/
├── manage.py
├── requirements.txt
├── build.sh
├── render.yaml
├── movie_theater_booking/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── bookings/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tests.py
│   └── templates/
│       └── bookings/
│           ├── base.html
│           ├── movie_list.html
│           ├── seat_booking.html
│           └── booking_history.html
└── features/
    ├── environment.py
    ├── bookings.feature
    └── steps/
        └── booking_steps.py

API Endpoints:
/api/movies/   List all movies or add one
/api/movies/<id>/   See or modify a specific added movie
/api/seats/     List all seats or add one
/api/seats/     List all available seats
/api/bookings/  View your account's bookings or add one
/api/bookings/  View or modify a specific booking

Running Tests
Unit & Integration Tests:
python manage.py test bookings

BDD Tests (Behave):
python -m behave

Deployment
This project is deployed on Render. To deploy your own instance:

Push the project to a GitHub repository
Create a new Web Service on render.com
Connect your GitHub repo and set the Root Directory to homework2
Set the Build Command to ./build.sh
Set the Start Command to gunicorn movie_theater_booking.wsgi:application
Deploy

AI Usage:
I used Claude a lot for this project, mostly helping me figure out errors
and showing me examples and formats for code, such as the tests and templates.
It wasn't perfect, and occasionaly I'd have to fix something it suggested, or after
giving it more context it'd change its suggestions
