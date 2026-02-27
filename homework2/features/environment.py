import django
from django.test.runner import DiscoverRunner
from django.test.utils import setup_test_environment

os_environ_setdefault = __import__('os').environ.setdefault
os_environ_setdefault('DJANGO_SETTINGS_MODULE', 'movie_theater_booking.settings')

django.setup()
setup_test_environment()

runner = DiscoverRunner(verbosity=0)

def before_all(context):
    context.old_config = runner.setup_databases()

def after_all(context):
    runner.teardown_databases(context.old_config)

def before_scenario(context, scenario):
    from django.test import Client
    from django.contrib.auth.models import User
    from bookings.models import Movie, Seat, Booking
    
    # Clear database before each scenario
    Booking.objects.all().delete()
    Seat.objects.all().delete()
    Movie.objects.all().delete()
    User.objects.all().delete()
    
    context.client = Client()