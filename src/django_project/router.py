from rest_framework.routers import DefaultRouter

from core.company.infra.company_django_app.router import router as company_router

from core.uploader.infra.uploader_django_app.router import router as uploader_router
from core.user.infra.user_django_app.router import router as user_router


router = DefaultRouter()
router.registry.extend(company_router.registry)

router.registry.extend(uploader_router.registry)
router.registry.extend(user_router.registry)

