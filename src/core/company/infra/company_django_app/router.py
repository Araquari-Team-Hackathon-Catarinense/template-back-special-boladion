from rest_framework.routers import DefaultRouter

from core.company.infra.company_django_app.views import CompanyViewSet

router = DefaultRouter()

router.register(r"companies", CompanyViewSet, basename="company")
