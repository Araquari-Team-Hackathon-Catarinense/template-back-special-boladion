from core.company.infra.django_app.models import Company
from core.populate.infra.resources.data_company import companies_data


def populate_companies() -> None:
    if Company.objects.exists():
        return

    companies_to_create: list[Company] = [Company(**data) for data in companies_data]
    Company.objects.bulk_create(companies_to_create)
