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
    r"measurement-units", MeasurementUnitViewSet, basename="measurement-unit"
)
router.register(r"packings", PackingViewSet, basename="packing")
router.register(
    r"purchase-sale-orders", PurchaseSaleOrderViewSet, basename="purchase-sale-order"
)
router.register(
    r"transport-contracts", TransportContractViewSet, basename="transport-contract"
)
router.register(r"trips", TripViewSet, basename="trip")
