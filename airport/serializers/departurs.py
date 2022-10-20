from rest_framework import serializers

from airport.models import Departure_city


class DeparturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departure_city
        fields = (
            'id',
            'departure_city'
        )