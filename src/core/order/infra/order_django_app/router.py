from rest_framework.routers import DefaultRouter

from core.order.infra.order_django_app.views import (
    MeasurementUnitViewSet,
    PackingViewSet,
)

router = DefaultRouter()

router.register(r"measurement-units", MeasurementUnitViewSet, basename="measurement-unit")
router.register(r"packings", PackingViewSet, basename="packing")
