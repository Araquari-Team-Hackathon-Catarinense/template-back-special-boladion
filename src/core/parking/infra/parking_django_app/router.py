from rest_framework.routers import DefaultRouter

from core.parking.infra.parking_django_app.views import (
    ParkingSectorViewSet,
    ParkingViewSet,
)

router = DefaultRouter()

router.register(r"parkings", ParkingViewSet, basename="parking")
router.register(r"parking-sectors", ParkingSectorViewSet, basename="parking-sector")
