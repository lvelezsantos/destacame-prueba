from rest_framework.routers import SimpleRouter, DefaultRouter
from transport.views import PlaceViewSet, DriverViewSet, BusViewSet, PassengerViewSet, RouteViewSet, ScheduleViewSet, \
    PassengerScheduleViewSet

router = DefaultRouter()

router.register('places', PlaceViewSet)
router.register('drivers', DriverViewSet)
router.register('buses', BusViewSet)
router.register('passengers', PassengerViewSet)
router.register('routes', RouteViewSet)
router.register('schedules', ScheduleViewSet)
router.register('passenger-schedules', PassengerScheduleViewSet)


urlpatterns = router.urls
