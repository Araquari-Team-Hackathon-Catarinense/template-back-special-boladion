from rest_framework.routers import DefaultRouter

from core.company.infra.company_django_app.views import (
    CompanyViewSet,
    ContractViewSet,
    EmployeeViewSet,
)

router = DefaultRouter()

router.register(r"company/companies", CompanyViewSet, basename="company-company")
router.register(r"company/contracts", ContractViewSet, basename="company-contract")
router.register(r"company/employees", EmployeeViewSet, basename="company-employee")
