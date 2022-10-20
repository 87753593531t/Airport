from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from airport.models import Flight
from airport.serializers import FlightCreateSerializer


class FlightViewSet(ModelViewSet):
    serializers_class = FlightCreateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Flight.objects.all()

    def get_serializer_class(self):
        serializer_class = FlightCreateSerializer

        if self.action == 'create':
            serializer_class = FlightCreateSerializer
        elif self.action == 'update':
            serializer_class = FlightCreateSerializer
        #
        return serializer_class