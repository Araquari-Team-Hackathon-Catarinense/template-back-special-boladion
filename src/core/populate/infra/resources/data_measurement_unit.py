import random
import re
import uuid

from faker import Faker
from pycpfcnpj import gen

from core.company.infra.company_django_app.models import Company

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
