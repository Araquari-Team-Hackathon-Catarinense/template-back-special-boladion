import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import Parking


@pytest.mark.django_db
class TestPatchParkingAPI:
    def test_patch_a_valid_parking(self) -> None:
        company: Company = baker.make(Company)

        parking: Parking = baker.make(Parking, company=company, slots=0)
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        url = f"/api/parkings/{str(parking.id)}/"

        new_data = {
            "description": "New Description",
        }

        response = APIClient().patch(url, new_data, format="json", **headers)

        expected_data = {
            "id": str(parking.id),
            "description": new_data["description"],
            "slots": parking.slots,
        }
        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_parking(self) -> None:
        company: Company = baker.make(Company)
        url = "/api/parkings/12345678-1234-1234-1234-123456789012/"
        new_data = {
            "description": "New Description",
            "company": "12345678-1234-1234-1234-123456789012",
        }
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        response = APIClient().patch(url, new_data, format="json", **headers)
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Parking matches the given query."
        }

    def test_if_throw_error_when_pass_a_invalid_company(self) -> None:
        company: Company = baker.make(Company)
        parking: Parking = baker.make(Parking, company=company)
        url = f"/api/parkings/{str(parking.id)}/"

        headers = {"HTTP_X_COMPANY_ID": str(company.id)}

        new_data = {
            "description": "New Description",
            "company": "12345678-1234-1234-1234-123456789012",
        }

        response = APIClient().patch(url, new_data, format="json", **headers)

        assert response.status_code == 400
        assert "company" in response.json()
        assert (
            f'Pk inválido "{new_data["company"]}" - objeto não existe.'
            in response.json()["company"][0]
        )

    def test_patch_a_parking_by_passing_the_slots(self) -> None:
        company: Company = baker.make(Company)

        parking: Parking = baker.make(Parking, company=company, slots=0)
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        url = f"/api/parkings/{str(parking.id)}/"

        new_data = {
            "description": "New Description",
            "slots": 10,
        }

        response = APIClient().patch(url, new_data, format="json", **headers)

        expected_data = {
            "id": str(parking.id),
            "description": new_data["description"],
            "slots": 0,
        }
        assert response.status_code == 200
        assert json.loads(response.content) == expected_data
