import random
import uuid

from faker import Faker

from core.company.infra.company_django_app.models import Company, ContractType

faker = Faker("pt_BR")


def generate_contract_data():
    contract_data = []

    companies = list(Company.objects.all())

    for company in companies:
        target_company = random.choice([c for c in companies if c.id != company.id])

        for _ in range(5):
            contract_data.append(
                {
                    "id": str(uuid.uuid4()),
                    "source_company_id": company.id,
                    "target_company_id": target_company.id,
                    "contract_type": random.choice(
                        [choice[0] for choice in ContractType]
                    ),
                }
            )

    return contract_data
