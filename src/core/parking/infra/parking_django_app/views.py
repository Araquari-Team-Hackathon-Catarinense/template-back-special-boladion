from rest_framework.viewsets import ModelViewSet

from core.parking.infra.parking_django_app.serializers import (
    ParkingCreateSerializer,
    ParkingDetailSerializer,
    ParkingListSerializer,
    ParkingSectorCreateSerializer,
    ParkingSectorListSerializer,
)

from .models import Parking, ParkingSector


class ParkingViewSet(ModelViewSet):
    queryset = Parking.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "list":
            return ParkingListSerializer
        elif self.action == "retrieve":
            return ParkingDetailSerializer
        return ParkingCreateSerializer


class ParkingSectorViewSet(ModelViewSet):
    queryset = ParkingSector.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return ParkingSectorListSerializer
        return ParkingSectorCreateSerializer
