from django.db import models
from django.utils.translation import ugettext_lazy as _


class Place(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Route(models.Model):
    source = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='sources')
    destination = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='destinations')

    def __str__(self):
        return f'{self.source} to {self.destination}'

    class Meta:
        unique_together = ('source', 'destination')


class Driver(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Bus(models.Model):
    name = models.CharField(max_length=50, unique=True)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    capacity = models.FloatField(default=10)

    def __str__(self):
        return f'{self.name} ({self.driver.name})'

    class Meta:
        verbose_name_plural = _('Buses')


class Passenger(models.Model):
    identification = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.identification} - {self.name}'


class Schedule(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    bus = models.ForeignKey('Bus', on_delete=models.CASCADE)
    route = models.ForeignKey('Route', on_delete=models.CASCADE, related_name='schedules')

    def __str__(self):
        return f'{self.route} ({self.bus}): {self.start} - {self.end}'


class PassengerSchedule(models.Model):
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE, related_name='passengers')
    passenger = models.ForeignKey('Passenger', on_delete=models.CASCADE)
    seat = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.schedule} - {self.passenger} ({self.seat})'

    class Meta:
        ordering = ('-id', )
        unique_together = ('schedule', 'seat')