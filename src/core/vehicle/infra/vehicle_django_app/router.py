from rest_framework.routers import DefaultRouter

from core.vehicle.infra.vehicle_django_app.views import BodyViewSet, ModalityViewSet

router = DefaultRouter()

router.register("bodies", BodyViewSet, basename="body")
router.register("modalities", ModalityViewSet, basename="modality")
