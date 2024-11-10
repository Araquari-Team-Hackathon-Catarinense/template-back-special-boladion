from core.company.infra.company_django_app.models import Company
from core.populate.infra.resources.data_company import companies_data
from core.user.infra.user_django_app.models import User


def populate_companies() -> None:
    if Company.objects.exists():
        return

    companies_to_create: list[Company] = [Company(**data) for data in companies_data]
    Company.objects.bulk_create(companies_to_create)
