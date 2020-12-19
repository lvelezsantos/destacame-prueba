from django.db.models import Count, F, Sum, IntegerField, FloatField, Avg, Case, When

from rest_framework.viewsets import ModelViewSet

from transport.filters import ScheduleFilter
from transport.models import Place, Driver, Bus, Passenger, Route, Schedule, PassengerSchedule
from transport.serializers import PlaceSerializer, DriverSerializer, BusSerializer, PassengerSerializer, \
    RouteSerializer, ScheduleSerializer, PassengerScheduleSerializer, ScheduleSerializerDetail


class PlaceViewSet(ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()


class DriverViewSet(ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


class BusViewSet(ModelViewSet):
    serializer_class = BusSerializer
    queryset = Bus.objects.all().select_related('driver')


class PassengerViewSet(ModelViewSet):
    serializer_class = PassengerSerializer
    queryset = Passenger.objects.all()


class RouteViewSet(ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Route.objects.all().select_related('source', 'destination').annotate(
        passengers=Count('schedules__passengers', distinct=True, output_field=FloatField()),
        schedules_count=Count('schedules', distinct=True, output_field=FloatField()),
        passenger_avg=Case(
            When(schedules_count=0, then=0),
            default=F('passengers') / F('schedules_count')
        )
    ).order_by('-passengers')


class ScheduleViewSet(ModelViewSet):
    serializer_class = ScheduleSerializer
    filter_class = ScheduleFilter
    queryset = Schedule.objects.all().annotate(
        passengers_count=Count('passengers', output_field=FloatField()),
        occupation=F('passengers_count') / F('bus__capacity') * 100.0
    ).select_related(
        'bus', 'bus__driver', 'route', 'route__source',
        'route__destination',
    ).order_by('start', 'end')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ScheduleSerializerDetail

        else:
            return super(ScheduleViewSet, self).get_serializer_class()


class PassengerScheduleViewSet(ModelViewSet):
    serializer_class = PassengerScheduleSerializer
    queryset = PassengerSchedule.objects.all()
