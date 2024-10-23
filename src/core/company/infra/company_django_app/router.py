from rest_framework.routers import DefaultRouter

from core.company.infra.company_django_app.views import (
    CompanyViewSet,
    ContractViewSet,
    EmployeeViewSet,
    PackingViewSet,
)

router = DefaultRouter()

router.register(r"companies", CompanyViewSet, basename="company")
router.register(r"contracts", ContractViewSet, basename="contract")
router.register(r"employees", EmployeeViewSet, basename="employee")
router.register(r"packings", PackingViewSet, basename="packing")
