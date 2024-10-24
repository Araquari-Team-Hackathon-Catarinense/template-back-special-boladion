import uuid
from faker import Faker

from core.company.infra.company_django_app.models import Company

faker = Faker("pt_BR")


def generate_packings():
    packings = []

    for company in Company.objects.all():
        for index in range(3):
            packing = {
                "id": str(uuid.uuid4()),
                "description": faker.word(),
                "company": company,
            }
            packings.append(packing)

    return packings
