from rest_framework.routers import DefaultRouter

from core.vehicle.infra.vehicle_django_app.views import (
    BodyViewSet,
    CompositionViewSet,
    ModalityViewSet,
    VehicleCompositionViewSet,
    VehicleViewSet,
)

router = DefaultRouter()

router.register("vehicle/bodies", BodyViewSet, basename="vehicle-body")
router.register("vehicle/modalities", ModalityViewSet, basename="vehicle-modality")
router.register("vehicle/vehicles", VehicleViewSet, basename="vehicle-vehicles")
router.register(
    "vehicle/compositions", CompositionViewSet, basename="vehicle-composition"
)
router.register(
    "vehicle/vehicle-composition",
    VehicleCompositionViewSet,
    basename="vehicle-vehicle_composition",
)
