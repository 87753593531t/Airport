from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from airport.models import Departure_city
from airport.serializers import DeparturesSerializer

class DeparturesViewSet(ModelViewSet):
    serializer_class = DeparturesSerializer
    permission_classes = [IsAuthenticated]
    queryset = Departure_city.objects.all()


    def post(self, request, *args, **kwargs):
        serializer = DeparturesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(Departure_city.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)