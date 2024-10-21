import uuid

import pytest
from pycpfcnpj import gen
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import Parking, ParkingSector


@pytest.mark.django_db
class TestParkingSectorListAPI:
    def test_create_a_valid_parking(self) -> None:
        url: str = "/api/parking-sectors/"
        cnpj: str = gen.cnpj()
        company: Company = Company.objects.create(
            name="Company 1",
            trade_name="Trade Name 1",
            person_type="PJ",
            is_active=True,
            document_number=cnpj,
        )

        parking: Parking = Parking.objects.create(
            description="Parking 1",
            company=company,
        )

        parking_sector = {
            "description": "Parking Sector 1",
            "sector_type": "ROTATIVE",
            "qty_slots": 100,
            "parking": str(parking.id),
        }

        response = APIClient().post(
            url,
            {
                "description": parking_sector["description"],
                "sector_type": parking_sector["sector_type"],
                "qty_slots": parking_sector["qty_slots"],
                "parking": parking_sector["parking"],
            },
        )

        assert response.status_code == 201
        assert response.json() == {
            "id": response.json()["id"],
            "description": parking_sector["description"],
            "sector_type": parking_sector["sector_type"],
            "qty_slots": parking_sector["qty_slots"],
            "contract": None,
            "parking": parking_sector["parking"],
        }

    def test_if_throw_error_with_invalid_parking(self) -> None:
        url = "/api/parking-sectors/"

        parking_sector = {
            "description": "Parking Sector 1",
            "sector_type": "ROTATIVE",
            "qty_slots": 100,
            "parking": str(uuid.uuid4()),
        }

        response = APIClient().post(
            url,
            {
                "description": parking_sector["description"],
                "sector_type": parking_sector["sector_type"],
                "qty_slots": parking_sector["qty_slots"],
                "parking": parking_sector["parking"],
            },
        )

        assert response.status_code == 400
        assert (
            f'Invalid pk "{parking_sector["parking"]}" - object does not exist.'
            in response.json()["parking"][0]
        )

    def test_if_create_a_parking_sector_by_passing_the_contract(
        self,
    ) -> None:
        url = "/api/parking-sectors/"

        cnpj: str = gen.cnpj()
        company: Company = Company.objects.create(
            name="Company 1",
            trade_name="Trade Name 1",
            person_type="PJ",
            is_active=True,
            document_number=cnpj,
        )

        parking: Parking = Parking.objects.create(
            description="Parking 1",
            company=company,
        )

        parking_sector = {
            "description": "Parking Sector 1",
            "sector_type": "CONTRACT",
            "qty_slots": 100,
            "parking": str(parking.id),
            "contract": 1,
        }

        response = APIClient().post(
            url,
            {
                "description": parking_sector["description"],
                "sector_type": parking_sector["sector_type"],
                "qty_slots": parking_sector["qty_slots"],
                "parking": parking_sector["parking"],
                "contract": parking_sector["contract"],
            },
        )

        print(response.content)
        assert response.status_code == 201
        assert response.json() == {
            "id": response.json()["id"],
            "description": parking_sector["description"],
            "sector_type": parking_sector["sector_type"],
            "qty_slots": parking_sector["qty_slots"],
            "contract": parking_sector["contract"],
            "parking": parking_sector["parking"],
        }
