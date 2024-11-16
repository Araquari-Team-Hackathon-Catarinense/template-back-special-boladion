import random
import uuid
from faker import Faker
from core.company.infra.company_django_app.models import Company, ContractType

faker = Faker("pt_BR")

def generate_contract_data():
    contract_data = []
    companies = list(Company.objects.all())
    contract_types = list(ContractType)

    for company in companies:
        for contract_type in contract_types:
            for _ in range(5):
                target_company = random.choice([c for c in companies if c.id != company.id])
                contract_data.append({
                    "id": uuid.uuid4(),
                    "source_company": company,
                    "target_company": target_company,
                    "contract_type": contract_type
                })

    return contract_data
