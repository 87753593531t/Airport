from rest_framework import serializers

from airport.models import Flight


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = (
            'id',
            'departures',
            'arrival',
            'flight_number',
            'aircraft_type',
            'time',
            'actual_time',
            'status'
        )


class FlightCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = (
            'id',
            'departures',
            'arrival',
            'flight_number',
            'aircraft_type',
            'time',
            'actual_time',
            'status'
        )