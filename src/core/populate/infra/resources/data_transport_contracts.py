import random
import traceback
import uuid
from datetime import datetime

from faker import Faker

from core.company.infra.company_django_app.models import Company, Contract
from core.order.infra.order_django_app.models import (
    PurchaseSaleOrder,
    TransportContract,
)
from core.populate.infra.resources.data_company import companies_data

faker = Faker("pt_BR")


# def to_iso_string(value):
#     if isinstance(value, datetime):
#         return value.isoformat()
#     return value
purchase_sale_orders = PurchaseSaleOrder.objects.all()


def generate_transports():
    transport_records = []
    for index, company_info in enumerate(companies_data):
        try:
            company = Company.objects.get(id=company_info["id"])
            carrier = Company.objects.exclude(id=company.id).first()

            if carrier is None:
                print(f"No carrier found for company ID: {company.id}")
                continue

            contract = Contract(
                id=str(uuid.uuid4()),
                source_company=company,
                target_company=carrier,
                contract_type="TRANSPORTADORA",
            )
            contract.save()

            purchase_sale_order = purchase_sale_orders[index]
            if index >= len(purchase_sale_orders):
                print(f"Index {index} is out of range for purchase_sale_orders")
                continue

            if not isinstance(purchase_sale_order, PurchaseSaleOrder):
                print(
                    f"purchase_sale_order não é uma instância de PurchaseSaleOrder: {purchase_sale_order}"
                )
                continue

            print(f"purchase_sale_order instância correta: {purchase_sale_order}")

            for _ in range(3):
                transport = {
                    "id": str(uuid.uuid4()),
                    "company": company,
                    "carrier": carrier,
                    "purchase_sale_order": purchase_sale_order,
                    "quantity": 10.0,
                    "balance": 10.0,
                }
                transport_records.append(transport)

        except Exception as e:
            print(f"An error occurred for company ID {company_info['id']}: {e}")

    return transport_records
