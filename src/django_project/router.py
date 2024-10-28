from rest_framework.routers import DefaultRouter

from core.company.infra.company_django_app.router import router as company_router
from core.order.infra.order_django_app.router import router as product_router
from core.parking.infra.parking_django_app.router import router as parking_router
from core.product.infra.product_django_app.router import router as product_router
from core.uploader.infra.uploader_django_app.router import router as uploader_router
from core.user.infra.user_django_app.router import router as user_router
from core.vehicle.infra.vehicle_django_app.router import router as vehicle_router

router = DefaultRouter()
router.registry.extend(company_router.registry)
router.registry.extend(parking_router.registry)
router.registry.extend(uploader_router.registry)
router.registry.extend(user_router.registry)
router.registry.extend(product_router.registry)
router.registry.extend(vehicle_router.registry)
