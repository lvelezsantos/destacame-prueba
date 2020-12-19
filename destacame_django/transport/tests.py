from datetime import datetime, timezone

import pytz
from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from transport.models import Place, Driver, Bus, Schedule, Route, PassengerSchedule, Passenger
from transport.views import PlaceViewSet


class TransportTest(APITestCase):

    def setUp(self):
        self.test_email = 'lvelezsantos@gmail.com'
        self.test_password = '12345678'

        self.test_user = get_user_model().objects.create(
            username='lvelez',
            email=self.test_email,
            is_active=True,
            first_name='Luis',
            last_name='Velez'
        )
        self.test_user.set_password(self.test_password)
        self.test_user.save(update_fields=('password',))
        self.test_token = Token.objects.create(user=self.test_user)

        self.auth_client = self.client_class()
        self.auth_client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_token.key)

        self.setup_site_data()

    def setup_site_data(self):
        self.place = Place.objects.create(name='Sincelejo')
        self.place_two = Place.objects.create(name='Bogota')
        self.driver = Driver.objects.create(name='Carlos')
        self.bus = Bus.objects.create(name='BUS01', driver=self.driver, capacity=2)
        self.route = Route.objects.create(source=self.place, destination=self.place_two)
        self.passenger = Passenger.objects.create(name='Luis', identification='123456')

        self.schedule = Schedule.objects.create(
            bus=self.bus,
            start=datetime(day=10, month=10, year=2020, hour=10, tzinfo=pytz.UTC),
            end=datetime(day=10, month=10, year=2020, hour=18, tzinfo=pytz.UTC),
            route=self.route,
        )

        self.schedule_two = Schedule.objects.create(
            bus=self.bus,
            start=datetime(day=10, month=10, year=2020, hour=20, tzinfo=pytz.UTC),
            end=datetime(day=10, month=10, year=2020, hour=21, tzinfo=pytz.UTC),
            route=self.route,
        )

        self.passenger_schedule = PassengerSchedule.objects.create(
            schedule=self.schedule,
            passenger=self.passenger,
            seat=1
        )



    def test_validate_unique_place_creation(self):
        response = self.auth_client.post(
            reverse('place-list'),
            {
                'name': 'sincelejo',
            }
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_schedule_creation(self):
        response = self.auth_client.post(
            reverse('schedule-list'),
            {
                'start': datetime(day=10, month=10, year=2020, hour=11, tzinfo=pytz.UTC),
                'end': datetime(day=10, month=10, year=2020, hour=17, tzinfo=pytz.UTC),
                'bus': self.bus.id,
                'route': self.route.id,
            }
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_schedule_creation_start_lower(self):
        response = self.auth_client.post(
            reverse('schedule-list'),
            {
                'start': datetime(day=10, month=10, year=2020, hour=9, tzinfo=pytz.UTC),
                'end': datetime(day=10, month=10, year=2020, hour=18, tzinfo=pytz.UTC),
                'bus': self.bus.id,
                'route': self.route.id,
            }
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_schedule_creation_end_greater(self):
        response = self.auth_client.post(
            reverse('schedule-list'),
            {
                'start': datetime(day=10, month=10, year=2020, hour=10, tzinfo=pytz.UTC),
                'end': datetime(day=10, month=10, year=2020, hour=19, tzinfo=pytz.UTC),
                'bus': self.bus.id,
                'route': self.route.id,
            }
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_schedule_creation_start_lower_end_greater(self):
        response = self.auth_client.post(
            reverse('schedule-list'),
            {
                'start': datetime(day=10, month=10, year=2020, hour=9, tzinfo=pytz.UTC),
                'end': datetime(day=10, month=10, year=2020, hour=19, tzinfo=pytz.UTC),
                'bus': self.bus.id,
                'route': self.route.id,
            }
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_validate_schedule_creation_start_lower_end_greater_two(self):
        response = self.auth_client.post(
            reverse('schedule-list'),
            {
                'start': datetime(day=10, month=10, year=2020, hour=19, tzinfo=pytz.UTC),
                'end': datetime(day=10, month=10, year=2020, hour=20, minute=22, tzinfo=pytz.UTC),
                'bus': self.bus.id,
                'route': self.route.id,
            }
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_schedule_creation_middle(self):
        response = self.auth_client.post(
            reverse('schedule-list'),
            {
                'start': datetime(day=10, month=10, year=2020, hour=19, minute=1, tzinfo=pytz.UTC),
                'end': datetime(day=10, month=10, year=2020, hour=19, minute=20, tzinfo=pytz.UTC),
                'bus': self.bus.id,
                'route': self.route.id,
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_schedule_creation_lower(self):
        response = self.auth_client.post(
            reverse('schedule-list'),
            {
                'start': datetime(day=10, month=10, year=2020, hour=7, minute=1, tzinfo=pytz.UTC),
                'end': datetime(day=10, month=10, year=2020, hour=7, minute=20, tzinfo=pytz.UTC),
                'bus': self.bus.id,
                'route': self.route.id,
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_schedule_creation_greater(self):
        response = self.auth_client.post(
            reverse('schedule-list'),
            {
                'start': datetime(day=10, month=10, year=2020, hour=21, minute=1, tzinfo=pytz.UTC),
                'end': datetime(day=10, month=10, year=2020, hour=21, minute=20, tzinfo=pytz.UTC),
                'bus': self.bus.id,
                'route': self.route.id,
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_validate_passenger_schedule_max_bus_capacity(self):
        self.passenger_schedule = PassengerSchedule.objects.create(
            schedule=self.schedule,
            passenger=self.passenger,
            seat=3
        )
        response = self.auth_client.post(
            reverse('passengerschedule-list'),
            {
                'passenger': self.passenger.id,
                'schedule': self.schedule.id,
                'seat': 2,
            }
        )

        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data,
            {'non_field_errors': ['The bus dont have available seats. The bus capacity is 2.0']}
        )

    def test_validate_passenger_schedule_seat(self):
        response = self.auth_client.post(
            reverse('passengerschedule-list'),
            {
                'passenger': self.passenger.id,
                'schedule': self.schedule.id,
                'seat': 3,
            }
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'non_field_errors': ['Please select a valid seat. the max number is 2.0']})
