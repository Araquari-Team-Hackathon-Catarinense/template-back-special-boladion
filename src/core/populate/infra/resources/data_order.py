import random
import uuid
from datetime import date

from faker import Faker

from core.company.infra.company_django_app.models import Company, Contract
from core.order.infra.order_django_app.models import (
    Composition,
    Driver,
    MeasurementUnit,
    Packing,
    PurchaseSaleOrder,
    TransportContract,
)
from core.product.infra.product_django_app.models import Product

faker = Faker("pt_BR")


def generate_measurement_units():
    measurement_units = []

    for company in Company.objects.all():
        for index in range(3):
            index += 1

            measurement_unit = {
                "id": str(uuid.uuid4()),
                "description": f"unit {index}",
                "company": company,
            }
            measurement_units.append(measurement_unit)

    return measurement_units


def generate_packings():
    packings = []

    for company in Company.objects.all():
        for _ in range(3):
            packing = {
                "id": str(uuid.uuid4()),
                "description": faker.word(),
                "company": company,
            }
            packings.append(packing)

    return packings


purchase_sale_orders = []


def generate_purchase_sale_orders():
    products_instances = Product.objects.all()
    purchase_sale_orders_data = []

    for company in Company.objects.all():
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

            purchase_sale_orders_data.append(purchase_sale_order_data)

    return purchase_sale_orders_data


# def to_iso_string(value):
#     if isinstance(value, datetime):
#         return value.isoformat()
#     return value
purchase_sale_orders = PurchaseSaleOrder.objects.all()


def generate_transports():
    transport_records = []
    for index, company in enumerate(Company.objects.all()):
        try:
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
            print(f"An error occurred for company ID {company.id}: {e}")

    return transport_records


def generate_trips():
    trips = []
    vehicles = Composition.objects.all()
    drivers = Driver.objects.all()

    for company in Company.objects.all():
        transport_contracts = TransportContract.objects.filter(company=company)
        if not transport_contracts.exists():
            print(f"No transport contracts found for company ID: {company.id}")
            continue

        for transport_contract in transport_contracts:

            for _ in range(3):

                if not vehicles.exists():
                    print("No vehicles found")
                    continue
                vehicle = random.choice(vehicles)

                if not drivers.exists():
                    print("No drivers found")
                    continue
                driver = random.choice(drivers)

                quantity = transport_contract.quantity / 4
                date = faker.date_between(start_date="-1y", end_date="today")
                order_number = faker.word()

                trip = {
                    "id": str(uuid.uuid4()),
                    "transport_contract": transport_contract,
                    "quantity": quantity,
                    "date": date,
                    "order_number": order_number,
                    "vehicle": vehicle,
                    "driver": driver,
                }
                trips.append(trip)

    return trips


composition_data = [
    {
        "id": str(uuid.uuid4()),
        "axle": 4,
        "gross_weight": 16000,
        "date": date(2021, 1, 1),
        "is_active": True,
    },
    {
        "id": str(uuid.uuid4()),
        "axle": 5,
        "gross_weight": 15000,
        "date": date(2021, 1, 1),
        "is_active": True,
    },
    {
        "id": str(uuid.uuid4()),
        "axle": 6,
        "gross_weight": 14000,
        "date": date(2021, 1, 1),
        "is_active": True,
    },
    {
        "id": str(uuid.uuid4()),
        "axle": 7,
        "gross_weight": 13000,
        "date": date(2021, 1, 1),
        "is_active": True,
    },
    {
        "id": str(uuid.uuid4()),
        "axle": 8,
        "gross_weight": 12000,
        "date": date(2021, 1, 1),
        "is_active": True,
    },
    {
        "id": str(uuid.uuid4()),
        "axle": 9,
        "gross_weight": 11000,
        "date": date(2021, 1, 1),
        "is_active": True,
    },
]
