from rest_framework.routers import DefaultRouter

from core.company.infra.django_app.router import router as company_router

router = DefaultRouter()
router.registry.extend(company_router.registry)
