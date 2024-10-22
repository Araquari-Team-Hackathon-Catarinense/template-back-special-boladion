from rest_framework.viewsets import ModelViewSet

from core.parking.infra.parking_django_app.serializers import (
    OperationCreateSerializer,
    OperationListSerializer,
    ParkingCreateSerializer,
    ParkingDetailSerializer,
    ParkingListSerializer,
    ParkingSectorCreateSerializer,
    ParkingSectorListSerializer,
)

from .models import Operation, Parking, ParkingSector


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


class OperationViewSet(ModelViewSet):
    queryset = Operation.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return OperationListSerializer
        return OperationCreateSerializer
