from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from transport.models import Place, Bus, Driver, Passenger, Route, Schedule, PassengerSchedule


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = ('id', 'name', 'description')

    def validate_name(self, value):
        if value:
            value = value.strip()
            places = Place.objects.filter(name__iexact=value)
            if self.instance:
                places = places.exclude(id=self.instance.id)

            if places.exists():
                raise serializers.ValidationError(_('place with this name already exists.'))

        return value


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = ('id', 'name', )


class BusSerializer(serializers.ModelSerializer):

    driver_info = DriverSerializer(read_only=True, source='driver')

    class Meta:
        model = Bus
        fields = ('id', 'name', 'driver', 'driver_info', 'capacity')


class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = ('id', 'name', 'identification')


class RouteSerializer(serializers.ModelSerializer):
    source_data = PlaceSerializer(read_only=True, source='source')
    destination_data = PlaceSerializer(read_only=True, source='destination')
    repr = serializers.SerializerMethodField()
    passengers = serializers.ReadOnlyField()
    schedules_count = serializers.ReadOnlyField()
    passenger_avg = serializers.ReadOnlyField()

    class Meta:
        model = Route
        fields = ('id', 'source', 'source_data', 'destination', 'destination_data', 'repr', 'passengers', 'schedules_count', 'passenger_avg')

    def validate(self, data):
        if data.get('source') == data.get('destination'):
            raise serializers.ValidationError(_('You cannot select the same source and destination'))

        return data

    def get_repr(self, obj):
        return str(obj)


class ScheduleSerializer(serializers.ModelSerializer):
    bus_data = BusSerializer(read_only=True, source='bus')
    route_data = RouteSerializer(read_only=True, source='route')
    passengers_count = serializers.SerializerMethodField()
    occupation = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = ('id', 'start', 'end', 'bus', 'bus_data', 'route', 'route_data', 'passengers_count', 'occupation')

    def get_passengers_count(self, obj):
        if hasattr(obj, 'passengers_count'):
            return obj.passengers_count

        else:
            return None

    def get_occupation(self, obj):
        if hasattr(obj, 'occupation'):
            return round(obj.occupation, 2)

        else:
            return None

    def validate(self, data):

        if data.get('end') < data.get('start'):
            raise serializers.ValidationError('Start cannot be greater than end')

        schedules = Schedule.objects.filter(
            bus=data.get('bus')
        )
        if self.instance:
            schedules = schedules.exclude(id=self.instance.id)

        schedules = schedules.filter(
            (Q(start__lte=data.get('start')) & Q(end__gte=data.get('start'))) |
            (Q(start__lte=data.get('end')) & Q(end__gte=data.get('end'))) |
            (Q(start__gte=data.get('start')) & Q(start__lte=data.get('end'))) |
            (Q(end__gte=data.get('start')) & Q(end__lte=data.get('end')))
        )

        if schedules.exists():
            raise serializers.ValidationError('you cannot make that schecdule for that route and bus')

        return data


class ScheduleSerializerDetail(ScheduleSerializer):
    passengers_list = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = (
            'id', 'start', 'end', 'bus', 'bus_data', 'route', 'route_data',
            'passengers_count', 'occupation', 'passengers_list'
        )

    def get_passengers_list(self, obj):
        data = PassengerScheduleSerializer(
            obj.passengers.all().select_related('passenger'),
            many=True, source='passengers', ).data

        return data


class PassengerScheduleSerializer(serializers.ModelSerializer):
    passenger_data = PassengerSerializer(read_only=True, source='passenger')

    class Meta:
        model = PassengerSchedule
        fields = ('id', 'schedule', 'passenger', 'passenger_data', 'seat', )

    def validate(self, data):

        schedule = data.get('schedule')
        seat = data.get('seat')
        if schedule and seat and seat > schedule.bus.capacity:
            raise serializers.ValidationError(f'Please select a valid seat. the max number is {schedule.bus.capacity}')

        if schedule and seat and schedule.passengers.count() >= schedule.bus.capacity:
            raise serializers.ValidationError(f'The bus dont have available seats. The bus capacity is {schedule.bus.capacity}')

        return data



