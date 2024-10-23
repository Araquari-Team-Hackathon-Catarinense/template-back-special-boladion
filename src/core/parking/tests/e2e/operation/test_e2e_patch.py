import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import Operation, Parking


@pytest.mark.django_db
class TestPatchOperationAPI:
    def test_patch_a_valid_operation(self) -> None:
        parking: Parking = baker.make(Parking)

        operation: Operation = baker.make(Operation, parking=parking)

        url = f"/api/operations/{str(operation.id)}/"

        new_data = {
            "name": "New Operation",
        }

        response = APIClient().patch(url, new_data, format="json")

        expected_data = {
            "id": str(operation.id),
            "name": new_data["name"],
            "parking": str(operation.parking.id),
        }
        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_operation(self) -> None:
        url = "/api/operations/12345678-1234-1234-1234-123456789012/"
        new_data = {
            "name": "New Name",
        }
        response = APIClient().patch(url, new_data, format="json")
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Operation matches the given query."
        }

    def test_if_throw_error_when_pass_a_invalid_parking(self) -> None:
        parking: Parking = baker.make(Parking)

        operation: Operation = baker.make(Operation, parking=parking)

        url = f"/api/operations/{str(operation.id)}/"

        new_data = {
            "name": "New name",
            "parking": "12345678-1234-1234-1234-123456789012",
        }

        response = APIClient().patch(url, new_data, format="json")

        assert response.status_code == 400
        assert "parking" in response.json()
        assert (
            f'Pk inválido "{new_data["parking"]}" - objeto não existe.'
            in response.json()["parking"][0]
        )
