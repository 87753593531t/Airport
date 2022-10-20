from rest_framework.routers import DefaultRouter
from rest_framework.urls import path

from airport.views import FlightViewSet, ArrivalViewSet, DeparturesViewSet

router = DefaultRouter()
router.register('flights', FlightViewSet)
router.register('arrival', ArrivalViewSet)
router.register('departures', DeparturesViewSet)
urlpatterns = [

]+router.urls