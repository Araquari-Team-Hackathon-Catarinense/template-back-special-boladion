from rest_framework.routers import DefaultRouter

from core.service.infra.service_django_app.views import ServiceViewSet

router = DefaultRouter()

router.register("services", ServiceViewSet, basename="service")
