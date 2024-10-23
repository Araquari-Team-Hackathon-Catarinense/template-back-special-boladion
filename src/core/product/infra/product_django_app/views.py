from product.infra.product_django_app.models import MeasurementUnit
from product.infra.product_django_app.serializers import (
    MeasurementUnitCreateSerializer,
    MeasurementUnitDetailSerializer,
    MeasurementUnitListSerializer,
)
from rest_framework.viewsets import ModelViewSet


class MeasurementUnitViewSet(ModelViewSet):
    queryset = MeasurementUnit.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MeasurementUnitDetailSerializer
        if self.action == "list":
            return MeasurementUnitListSerializer
        return MeasurementUnitCreateSerializer
