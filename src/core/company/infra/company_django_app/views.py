from drf_spectacular.utils import extend_schema
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


@extend_schema(tags=["Core"])
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

    @action(detail=True, methods=["post"], url_path="upload-avatar")
    def upload_avatar(self, request, pk=None):
        try:
            company: Company = self.get_object()
            data = request.data.copy()
            if (
                "description" not in data
                or data["description"] is None
                or data["description"] == ""
            ):
                data["description"] = f"Avatar da empresa {company.name}"
            data["file"] = request.FILES.get("file")
            serializer = DocumentUploadSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            if company.avatar:
                company.avatar.delete()
            company.avatar = serializer.instance
            company.save()
            return super().retrieve(request)
        except Exception as e:
            print(e)
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["Company"])
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


@extend_schema(tags=["Company"])
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
