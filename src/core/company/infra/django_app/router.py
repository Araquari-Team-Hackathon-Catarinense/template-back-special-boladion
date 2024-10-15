from rest_framework.routers import DefaultRouter

from core.company.infra.django_app.views import CompanyViewSet

router = DefaultRouter()

router.register(r"companies", CompanyViewSet, basename="company")
