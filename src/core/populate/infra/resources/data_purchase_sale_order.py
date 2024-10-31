import random
import uuid

from faker import Faker

from core.company.infra.company_django_app.models import Company
from core.order.infra.order_django_app.models import (
    MeasurementUnit,
    Packing,
    PurchaseSaleOrder,
)
from core.product.infra.product_django_app.models import Product

faker = Faker("pt_BR")

from core.populate.infra.resources.data_company import companies_data

purchase_sale_orders = []


def generate_purchase_sale_orders():
    products_instances = Product.objects.all()
    purchase_sale_orders_data = []

    for company_data in companies_data:
        company = Company.objects.get(id=company_data["id"])
        client = random.choice(Company.objects.exclude(id=company.id))
        operation_terminal = random.choice(Company.objects.exclude(id=company.id))

        for _ in range(random.randint(3, 10)):
            product = random.choice(products_instances)
            measurement_unit = random.choice(MeasurementUnit.objects.all())
            packing = random.choice(Packing.objects.all())
            operation_type = random.choice(
                [choice[0] for choice in PurchaseSaleOrder.OPERATION_TYPE_CHOICES]
            )

            purchase_sale_order_data = {
                "id": uuid.uuid4(),
                "company": company,
                "client": client,
                "product": product,
                "measurement_unit": measurement_unit,
                "packing": packing,
                "quantity": round(random.uniform(1, 100), 2),
                "balance": round(random.uniform(0, 50), 2),
                "operation_terminal": operation_terminal,
                "operation_type": operation_type,
            }

            purchase_sale_orders_data.append(
                purchase_sale_order_data
            )  # Adiciona o dicionário à lista

    return purchase_sale_orders_data
