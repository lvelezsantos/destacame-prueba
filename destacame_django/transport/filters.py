from django_filters import rest_framework as filters

from transport.models import Bus


class ScheduleFilter(filters.FilterSet):
    occupation = filters.NumberFilter(field_name="occupation", lookup_expr='gte', label='Occupation')
    bus = filters.ModelChoiceFilter(field_name="bus", lookup_expr='exact', label='Bus', queryset=Bus.objects.all())
