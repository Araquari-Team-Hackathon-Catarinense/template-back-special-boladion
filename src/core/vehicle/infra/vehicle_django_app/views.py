from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.uploader.infra.uploader_django_app.models import Document
from core.uploader.infra.uploader_django_app.serializers import DocumentUploadSerializer
from core.vehicle.infra.vehicle_django_app.models import (
    Body,
    Composition,
    Modality,
    Vehicle,
)
from core.vehicle.infra.vehicle_django_app.serializers import (
    BodyCreateSerializer,
    BodyListSerializer,
    CompositionCreateSerializer,
    CompositionDetailSerializer,
    CompositionListSerializer,
    ModalityCreateSerializer,
    ModalityListSerializer,
    VehicleCreateSerializer,
    VehicleDetailSerializer,
    VehicleListSerializer,
)


class BodyViewSet(ModelViewSet):
    queryset = Body.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return BodyListSerializer
        return BodyCreateSerializer


class ModalityViewSet(ModelViewSet):
    queryset = Modality.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ModalityListSerializer
        return ModalityCreateSerializer


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "list":
            return VehicleListSerializer
        if self.action == "retrieve":
            return VehicleDetailSerializer
        return VehicleCreateSerializer

    @action(detail=True, methods=["post"], url_path="upload-documents")
    def upload_documents(self, request, pk=None):
        vehicle = self.get_object()

        data = request.data.copy()
        data["file"] = request.FILES.get("file")
        serializer = DocumentUploadSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        vehicle.documents.add(serializer.instance)
        return Response(
            {"message": "Documento adicionado com sucesso"},
            status=status.HTTP_201_CREATED,
        )


class CompositionViewSet(ModelViewSet):
    queryset = Composition.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "list":
            return CompositionListSerializer
        elif self.action == "retrieve":
            return CompositionDetailSerializer
        return CompositionCreateSerializer
