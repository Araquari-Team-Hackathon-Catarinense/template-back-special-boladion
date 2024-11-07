from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.uploader.infra.uploader_django_app.serializers import DocumentUploadSerializer
from core.vehicle.infra.vehicle_django_app.models import (
    Body,
    Composition,
    Modality,
    Vehicle,
    VehicleComposition,
)
from core.vehicle.infra.vehicle_django_app.serializers import (
    BodyCreateSerializer,
    BodyListSerializer,
    CompositionCreateSerializer,
    CompositionDetailSerializer,
    CompositionListSerializer,
    ModalityCreateSerializer,
    ModalityListSerializer,
    VechicleCompositionCreateSerializer,
    VehicleCompositionListSerializer,
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


# class VehicleCompositionViewSet(ModelViewSet):
#     queryset = VehicleComposition.objects.all()
#     http_method_names = ["get"]

#     def get_serializer_class(self):
#         if self.action == "list":
#             return VehicleCompositionListSerializer
#         return VehicleCompositionListSerializer


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="license",
            type=str,
            location=OpenApiParameter.QUERY,
            required=True,
        )
    ]
)
class VehicleCompositionApiView(APIView):
    def get(self, request) -> Response:
        license_plates = request.query_params.getlist("license")

        if not license_plates:
            return Response(
                {"error": "(license) deve ser fornecida."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        vehicles: Vehicle = Vehicle.objects.filter(license__in=license_plates)

        compositions: Composition = Composition.objects.filter(
            id__in=VehicleComposition.objects.filter(vehicle__in=vehicles).values_list(
                "composition", flat=True
            )
        ).distinct()

        serializer: VehicleCompositionListSerializer = VehicleCompositionListSerializer(
            compositions, many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class VehicleCompositionViewSet(ModelViewSet):
    queryset = VehicleComposition.objects.all()
    http_method_names = ["post"]

    def get_serializer_class(self):

        return VechicleCompositionCreateSerializer
