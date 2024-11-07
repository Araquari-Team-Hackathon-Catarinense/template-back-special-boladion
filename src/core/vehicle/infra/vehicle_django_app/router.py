from rest_framework.routers import DefaultRouter

from core.vehicle.infra.vehicle_django_app.views import (
    BodyViewSet,
    CompositionViewSet,
    ModalityViewSet,
    VehicleCompositionViewSet,
    VehicleViewSet,
)

router = DefaultRouter()

router.register("bodies", BodyViewSet, basename="body")
router.register("modalities", ModalityViewSet, basename="modality")
router.register("vehicles", VehicleViewSet, basename="vehicle")
router.register("compositions", CompositionViewSet, basename="composition")
router.register(
    "vehicle-composition", VehicleCompositionViewSet, basename="vehicle_composition"
)
