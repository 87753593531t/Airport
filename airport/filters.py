from django_filters import rest_framework as filters


from airport.models import Flight
from airport.const import STATUSChoice

class FlightFilter(filters.FilterSet):
    city = filters.CharFilter(field_name='city', lookup_expr='exact', label='Город')
    flight_number = filters.NumberFilter(field_name='flight_number', lookup_expr='contains', label='Номер рейса')
    aircraft_type = filters.CharFilter(field_name='aircraft_type', lookup_expr='exact', label='Тип самолета')
    status = filters.ChoiceFilter(field_name='status', lookup_expr='exact', choices=STATUSChoice.choice(), label='Статус')

    class Meta:
        model = Flight
        fields=('city', 'flight_number', 'aircraft_type', 'status')