from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.__seedwork__.domain.exceptions import CompanyNotInHeader
from core.company.infra.company_django_app.filters import CompanyFilter, ContractFilter
from core.company.infra.company_django_app.serializers import (
    CompanyCreateSerializer,
    CompanyDetailSerializer,
    CompanyListSerializer,
    ContractCreateSerializer,
    ContractListSerializer,
    EmployeeCreateSerializer,
    EmployeeListSerializer,
)
from core.uploader.infra.uploader_django_app.models import Document
from core.uploader.infra.uploader_django_app.serializers import DocumentUploadSerializer

from .models import Company, Contract, Employee


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = CompanyFilter

    def get_serializer_class(self):
        if self.action == "list":
            return CompanyListSerializer
        elif self.action == "retrieve":
            return CompanyDetailSerializer
        return CompanyCreateSerializer

    @action(detail=True, methods=["post"], url_path="upload-documents")
    def upload_documents(self, request, pk=None):
        data = request.data.copy()
        data["file"] = request.FILES.get("file")
        serializer = DocumentUploadSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        company: Company = self.get_object()
        company.documents.add(serializer.instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        company_id = getattr(self.request, "company_id", None)

        if company_id:
            return Employee.objects.filter(company__id=company_id)
        raise CompanyNotInHeader

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return EmployeeListSerializer
        return EmployeeCreateSerializer


class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = ContractFilter

    def get_queryset(self):
        company_id = self.request.headers.get("X-Company-Id", None)
        if company_id:
            return Contract.objects.filter(source_company__id=company_id)
        raise CompanyNotInHeader

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ContractListSerializer
        return ContractCreateSerializer
