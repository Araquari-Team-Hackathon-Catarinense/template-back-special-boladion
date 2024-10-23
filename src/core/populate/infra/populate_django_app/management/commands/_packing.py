import uuid

from core.company.infra.company_django_app.models import Company, Packing
from core.populate.infra.resources.data_packing import packing_data


def populate_packings() -> None:
    if Packing.objects.exists():
        return

    packing_to_create: list[Packing] = [Packing(**data) for data in packing_data]
    company = Company.objects.first()
    for packing in packing_to_create:
        packing.id = uuid.uuid4
        packing.company = company

    Packing.objects.bulk_create(packing_to_create)
