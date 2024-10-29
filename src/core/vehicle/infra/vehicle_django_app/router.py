from rest_framework.routers import DefaultRouter

from core.vehicle.infra.vehicle_django_app.views import BodyViewSet

router = DefaultRouter()

router.register("bodies", BodyViewSet, basename="body")
