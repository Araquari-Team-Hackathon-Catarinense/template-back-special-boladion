from rest_framework.viewsets import ModelViewSet

from core.__seedwork__.domain.exceptions import CompanyNotInHeader
from core.order.infra.order_django_app.filters import (
    MeasurementUnitFilter,
    PackingFilter,
    PurchaseSaleOrderFilter,
)
from core.order.infra.order_django_app.models import (
    MeasurementUnit,
    Packing,
    PurchaseSaleOrder,
    TransportContract,
)
from core.order.infra.order_django_app.serializers import (
    MeasurementUnitCreateSerializer,
    MeasurementUnitListSerializer,
    PackingCreateSerializer,
    PackingListSerializer,
    PurchaseSaleOrderCreateSerializer,
    PurchaseSaleOrderListSerializer,
    TransportContractCreateSerializer,
    TransportContractListSerializer,
)


class MeasurementUnitViewSet(ModelViewSet):
    queryset = MeasurementUnit.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = MeasurementUnitFilter

    def get_queryset(self):
        company_id = getattr(self.request, "company_id", None)

        if company_id:
            return MeasurementUnit.objects.filter(company__id=company_id)
        raise CompanyNotInHeader

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return MeasurementUnitListSerializer
        return MeasurementUnitCreateSerializer


class PackingViewSet(ModelViewSet):
    queryset = Packing.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = PackingFilter

    def get_queryset(self):
        company_id = getattr(self.request, "company_id", None)

        if company_id:
            return Packing.objects.filter(company__id=company_id)
        raise CompanyNotInHeader

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PackingListSerializer
        return PackingCreateSerializer


class PurchaseSaleOrderViewSet(ModelViewSet):
    queryset = PurchaseSaleOrder.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = PurchaseSaleOrderFilter

    def get_queryset(self):
        company_id = getattr(self.request, "company_id", None)

        if company_id:
            return PurchaseSaleOrder.objects.filter(company__id=company_id)
        raise CompanyNotInHeader

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PurchaseSaleOrderListSerializer
        return PurchaseSaleOrderCreateSerializer


class TransportContractViewSet(ModelViewSet):
    queryset = TransportContract.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        company_id = self.request.headers.get("X-Company-Id", None)
        if company_id:
            return TransportContract.objects.filter(company__id=company_id)
        raise CompanyNotInHeader

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TransportContractListSerializer
        return TransportContractCreateSerializer
