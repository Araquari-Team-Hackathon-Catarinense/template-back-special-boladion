import random
import uuid

from faker import Faker

from core.company.infra.company_django_app.models import Company

faker = Faker("pt_BR")

from core.populate.infra.resources.data_company import companies_data

products = []


def generate_products():
    for company in companies_data:
        company = Company.objects.get(id=company["id"])
        for index in range(random.randint(1, 5)):
            product = {
                "id": str(uuid.uuid4()),
                "description": f"Product {index}",
                "internal_code": faker.unique.random_number(digits=10),
                "company": company,
            }
            products.append(product)

    return products
