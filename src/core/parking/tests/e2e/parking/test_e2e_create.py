import uuid

import pytest
from pycpfcnpj import gen
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import Parking


@pytest.mark.django_db
class TestListAPI:
    def test_create_a_valid_parking(self) -> None:
        url: str = "/api/parkings/"
        cnpj: str = gen.cnpj()
        company: Company = Company.objects.create(
            name="Company 1",
            trade_name="Trade Name 1",
            person_type="PJ",
            is_active=True,
            document_number=cnpj,
        )

        parking = {
            "description": "Parking 1",
            "entity": company.id,
        }

        response = APIClient().post(
            url,
            {
                "description": parking["description"],
                "entity": parking["entity"],
            },
        )

        assert response.status_code == 201
        assert response.json()["description"] == parking["description"]
        assert response.json()["entity"] == str(parking["entity"])
        assert "id" in response.json()

    def test_if_throw_error_with_invalid_entity(self) -> None:
        url = "/api/parkings/"

        parking = {
            "description": "Parking 1",
            "entity": uuid.uuid4(),
        }

        response = APIClient().post(
            url,
            {
                "description": parking["description"],
                "entity": parking["entity"],
            },
        )

        assert response.status_code == 400
        assert "entity" in response.json()
        assert (
            f'Invalid pk "{parking["entity"]}" - object does not exist.'
            in response.json()["entity"][0]
        )

    def test_if_create_a_parking_by_passing_the_slots(
        self,
    ) -> None:
        url = "/api/parkings/"

        company: Company = Company.objects.create(
            name="Company 1",
            trade_name="Trade Name 1",
            person_type="PJ",
            is_active=True,
            document_number=gen.cnpj(),
        )

        parking = {
            "description": "Parking 1",
            "entity": str(company.id),
            "slots": 100,
        }

        response = APIClient().post(
            url,
            {
                "description": parking["description"],
                "entity": parking["entity"],
                "slots": parking["slots"],
            },
        )

        assert response.status_code == 201
        assert "slots" in response.json()
        assert response.json()["slots"] == 0
