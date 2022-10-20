from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from airport.models import Arrival_city
from airport.serializers import ArrivalSerializer


class ArrivalViewSet(ModelViewSet):
    serializer_class = ArrivalSerializer
    permission_classes = [IsAuthenticated]
    queryset = Arrival_city.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = ArrivalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(Arrival_city.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
