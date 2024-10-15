from core.company.infra.django_app.serializers import (
    CompanyCreateSerializer,
    CompanyDetailSerializer,
    CompanyListSerializer,
)
from rest_framework.viewsets import ModelViewSet

from .models import Company


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "list":
            return CompanyListSerializer
        elif self.action == "retrieve":
            return CompanyDetailSerializer
        return CompanyCreateSerializer
