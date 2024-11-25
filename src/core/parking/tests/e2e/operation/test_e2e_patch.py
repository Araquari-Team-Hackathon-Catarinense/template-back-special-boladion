import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import Operation, Parking
from django_project.settings import API_VERSION


@pytest.mark.django_db
class TestPatchOperationAPI:
    def test_patch_a_valid_operation(self) -> None:
        company = baker.make(Company)
        parking: Parking = baker.make(Parking, company=company)

        operation: Operation = baker.make(Operation, parking=parking)
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        url = f"/api/{API_VERSION}/parking/operations/{str(operation.id)}/"

        new_data = {
            "name": "New Operation",
        }

        response = APIClient().patch(url, new_data, format="json", **headers)

        expected_data = {
            "id": str(operation.id),
            "name": new_data["name"],
            "parking": str(operation.parking.id),
        }
        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_operation(self) -> None:
        company = baker.make(Company)
        url = f"/api/{API_VERSION}/parking/operations/12345678-1234-1234-1234-123456789012/"
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        new_data = {
            "name": "New Name",
        }
        response = APIClient().patch(url, new_data, format="json", **headers)
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Operation matches the given query."
        }

    def test_if_throw_error_when_pass_a_invalid_parking(self) -> None:
        company = baker.make(Company)
        parking: Parking = baker.make(Parking, company=company)

        operation: Operation = baker.make(Operation, parking=parking)
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        url = f"/api/{API_VERSION}/parking/operations/{str(operation.id)}/"

        new_data = {
            "name": "New name",
            "parking": "12345678-1234-1234-1234-123456789012",
        }

        response = APIClient().patch(url, new_data, format="json", **headers)

        assert response.status_code == 400
        assert "parking" in response.json()
        assert (
            f'Pk inválido "{new_data["parking"]}" - objeto não existe.'
            in response.json()["parking"][0]
        )
