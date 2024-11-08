from rest_framework.routers import DefaultRouter

from core.parking.infra.parking_django_app.views import (
    OperationViewSet,
    ParkingSectorViewSet,
    ParkingViewSet,
)

router = DefaultRouter()

router.register(r"parking/parkings", ParkingViewSet, basename="parking-parking")
router.register(
    r"parking/parking-sectors", ParkingSectorViewSet, basename="parking-parking-sector"
)
router.register(r"parking/operations", OperationViewSet, basename="parking-operation")
