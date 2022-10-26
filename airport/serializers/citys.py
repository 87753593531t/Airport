from rest_framework import serializers


from airport.models import City


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'departures', 'arrival')