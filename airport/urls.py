from rest_framework.routers import DefaultRouter
from rest_framework.urls import path

from airport.views import FlightViewSet, CityViewSet

router = DefaultRouter()
router.register('flights', FlightViewSet)
router.register('citys', CityViewSet)
urlpatterns = []+router.urls