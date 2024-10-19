from rest_framework.viewsets import ModelViewSet

from core.company.infra.company_django_app.serializers import (
    CompanyCreateSerializer,
    CompanyDetailSerializer,
    CompanyListSerializer,
    EmployeeCreateSerializer,
    EmployeeListSerializer,
)

from .models import Company, Employee


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "list":
            return CompanyListSerializer
        elif self.action == "retrieve":
            return CompanyDetailSerializer
        return CompanyCreateSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return EmployeeListSerializer
        return EmployeeCreateSerializer
