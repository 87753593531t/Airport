from rest_framework import serializers

from airport.models import Arrival_city


class ArrivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arrival_city
        fields = (
            'id',
            'arrival_city'
        )