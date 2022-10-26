from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from airport.models import City
from airport.serializers import CitySerializer


class CityViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()

    def get_serializer_class(self):
        serializer_class = CitySerializer

        if self.action == 'create':
            serializer_class = CitySerializer
        elif self.action == 'update_attachments':
            serializer_class = CitySerializer
        elif self.action == 'delete_attachments':
            serializer_class = CitySerializer
        elif self.action == 'list':
            serializer_class = CitySerializer
        return serializer_class
