from django.contrib import admin

# Register your models here.
from transport.models import Place, Driver, Bus, Passenger, Route, Schedule, PassengerSchedule


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'source', 'destination')
    # raw_id_fields = ('source', 'destination')
    search_fields = ('route__name', 'route__destination')



class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class PassengerAdmin(admin.ModelAdmin):
    list_display = ('id', 'identification', 'name')


class BusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'driver', 'capacity')
    list_filter = ('driver', )

    raw_id_fields = ('driver', )
    search_fields = ('name', 'driver__name')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'start', 'end', 'bus', 'route')


class PassengerScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'schedule', 'passenger', 'seat', )
    raw_id_fields = ('schedule', 'passenger')


admin.site.register(Place, PlaceAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Passenger, PassengerAdmin)
admin.site.register(Bus, BusAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(PassengerSchedule, PassengerScheduleAdmin)