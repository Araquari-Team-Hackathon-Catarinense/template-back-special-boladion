from rest_framework.routers import DefaultRouter

from core.product.infra.product_django_app.views import MeasurementUnitViewSet

router = DefaultRouter()

router.register(r"measurement-units", MeasurementUnitViewSet)
