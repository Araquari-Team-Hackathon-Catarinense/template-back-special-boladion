from core.company.infra.django_app.serializers import (
    CompanyCreateSerializer,
    CompanyListSerializer,
)
from rest_framework.viewsets import ModelViewSet

from .models import Company


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CompanyListSerializer
        elif self.action == "create":
            return CompanyCreateSerializer
        return CompanyListSerializer
