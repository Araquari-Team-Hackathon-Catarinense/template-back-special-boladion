from rest_framework.viewsets import ModelViewSet

from core.vehicle.infra.vehicle_django_app.models import Body
from core.vehicle.infra.vehicle_django_app.serializers import (
    BodyCreateSerializer,
    BodyListSerializer,
)


class BodyViewSet(ModelViewSet):
    queryset = Body.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return BodyListSerializer
        return BodyCreateSerializer
