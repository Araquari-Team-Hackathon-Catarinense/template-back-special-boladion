from rest_framework.viewsets import ModelViewSet

from core.service.infra.service_django_app.models import Service
from core.service.infra.service_django_app.serializers import (
    ServiceCreateSerializer,
    ServiceListSerializer,
)


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ServiceListSerializer
        return ServiceCreateSerializer
