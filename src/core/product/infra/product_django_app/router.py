from rest_framework.routers import DefaultRouter

from core.product.infra.product_django_app.views import (
    MeasurementUnitViewSet,
    PackingViewSet,
)

router = DefaultRouter()

router.register(
    r"measurement-units", MeasurementUnitViewSet, basename="measurement-unit"
)


router.register(r"packing", PackingViewSet, basename="packing")
