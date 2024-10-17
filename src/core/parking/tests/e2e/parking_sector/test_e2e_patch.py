import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import Parking, ParkingSector


@pytest.mark.django_db
class TestPatchParkingSectorAPI:
    def test_patch_a_valid_parking_sector(self) -> None:
        company: Company = baker.make(Company)

        parking: Parking = baker.make(Parking, entity=company, slots=0)

        parking_sector: ParkingSector = baker.make(
            ParkingSector, parking=parking, sector_type="ROTATIVE"
        )

        url = f"/api/parking-sectors/{str(parking_sector.id)}/"

        new_data = {
            "description": "New Description",
            "qty_slots": 10,
        }

        response = APIClient().patch(url, new_data, format="json")

        expected_data = {
            "id": str(parking_sector.id),
            "description": new_data["description"],
            "sector_type": parking_sector.sector_type,
            "qty_slots": new_data["qty_slots"],
            "contract": None,
            "parking": str(parking_sector.parking.id),
        }
        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_parking_sector(self) -> None:
        url = "/api/parking-sectors/12345678-1234-1234-1234-123456789012/"
        new_data = {
            "description": "New Description",
            "qty_slots": 10,
        }
        response = APIClient().patch(url, new_data, format="json")
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No ParkingSector matches the given query."
        }

    def test_if_throw_error_when_pass_a_invalid_parking(self) -> None:
        parking: Parking = baker.make(Parking)

        parking_sector: ParkingSector = baker.make(
            ParkingSector, parking=parking, sector_type="ROTATIVE"
        )

        url = f"/api/parking-sectors/{str(parking_sector.id)}/"

        new_data = {
            "description": "New Description",
            "parking": "12345678-1234-1234-1234-123456789012",
        }

        response = APIClient().patch(url, new_data, format="json")

        assert response.status_code == 400
        assert "parking" in response.json()
        assert (
            f'Invalid pk "{new_data["parking"]}" - object does not exist.'
            in response.json()["parking"][0]
        )

    def test_patch_a_parking_by_passing_the_contract_with_sector_type_rotative(
        self,
    ) -> None:
        company: Company = baker.make(Company)

        parking: Parking = baker.make(Parking, entity=company, slots=0)

        parking_sector: ParkingSector = baker.make(
            ParkingSector, parking=parking, sector_type="CONTRACT", contract=10
        )

        url = f"/api/parking-sectors/{str(parking_sector.id)}/"

        new_data = {"description": "New Description", "sector_type": "ROTATIVE"}

        response = APIClient().patch(url, new_data, format="json")

        expected_data = {
            "id": str(parking_sector.id),
            "description": new_data["description"],
            "sector_type": new_data["sector_type"],
            "qty_slots": parking_sector.qty_slots,
            "parking": str(parking_sector.parking.id),
            "contract": None,
        }
        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_patch_a_parking_by_passing_the_contract_with_sector_type_contract(
        self,
    ) -> None:
        company: Company = baker.make(Company)

        parking: Parking = baker.make(Parking, entity=company, slots=0)

        parking_sector: ParkingSector = baker.make(
            ParkingSector, parking=parking, sector_type="ROTATIVE"
        )

        url = f"/api/parking-sectors/{str(parking_sector.id)}/"

        new_data = {
            "description": "New Description",
            "sector_type": "CONTRACT",
            "contract": 10,
        }

        response = APIClient().patch(url, new_data, format="json")

        expected_data = {
            "id": str(parking_sector.id),
            "description": new_data["description"],
            "sector_type": new_data["sector_type"],
            "qty_slots": parking_sector.qty_slots,
            "parking": str(parking_sector.parking.id),
            "contract": 10,
        }
        assert response.status_code == 200
        assert json.loads(response.content) == expected_data
