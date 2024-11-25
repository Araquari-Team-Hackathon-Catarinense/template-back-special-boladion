from rest_framework.routers import DefaultRouter

from core.order.infra.order_django_app.views import (
    MeasurementUnitViewSet,
    PackingViewSet,
    PurchaseSaleOrderViewSet,
    TransportContractViewSet,
    TripViewSet,
)

router = DefaultRouter()

router.register(
    r"order/measurement-units",
    MeasurementUnitViewSet,
    basename="order-measurement-unit",
)
router.register(r"order/packings", PackingViewSet, basename="order-packing")
router.register(
    r"order/purchase-sale-orders",
    PurchaseSaleOrderViewSet,
    basename="order-purchase-sale-order",
)
router.register(
    r"order/transport-contracts",
    TransportContractViewSet,
    basename="order-transport-contract",
)
router.register(r"order/trips", TripViewSet, basename="order-trip")
