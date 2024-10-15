from core.company.infra.django_app.serializers import (
    CompanyCreateSerializer,
    CompanyDetailSerializer,
    CompanyListSerializer,
)
from rest_framework.viewsets import ModelViewSet

from .models import Company


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CompanyListSerializer
        elif self.action == "retrieve":
            return CompanyDetailSerializer
        elif self.action == "create":
            return CompanyCreateSerializer
        return CompanyListSerializer
