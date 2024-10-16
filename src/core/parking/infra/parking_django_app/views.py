from rest_framework.viewsets import ModelViewSet

from core.parking.infra.parking_django_app.serializers import (
    ParkingCreateSerializer,
    ParkingListSerializer,
    ParkingDetailSerializer
)

from .models import Parking

class ParkingViewSet(ModelViewSet):
    queryset = Parking.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "list":
            return ParkingListSerializer
        elif self.action == "retrieve":
            return ParkingDetailSerializer
        return ParkingCreateSerializer
