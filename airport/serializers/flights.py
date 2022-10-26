import datetime

from rest_framework import serializers

from airport.models import Flight
from airport.const import STATUSChoice


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = (
            'id',
            'city',
            'flight_number',
            'aircraft_type',
            'time',
            'actual_time',
            'status'
        )


class FlightCreateSerializer(serializers.ModelSerializer):
    # status = serializers.SerializerMethodField('get_status')
    #
    # def get_status(self, instance):
    #     from datetime import timedelta, datetime
    #     if instance.time < datetime.now():
    #         instance.status = STATUSChoice.FLEW_OUT.value
    #         instance.save(update_fields=['status'])
    #         return STATUSChoice.FLEW_OUT.value

    class Meta:
        model = Flight
        fields = (
            'id',
            'city',
            'flight_number',
            'aircraft_type',
            'time',
            'actual_time',
            'status'
        )