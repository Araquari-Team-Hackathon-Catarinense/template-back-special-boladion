import uuid

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.parking.infra.parking_django_app.models import Parking

url = "/api/operations/"


@pytest.mark.django_db
class TestOperationListAPI:
    def test_create_a_valid_operation(self) -> None:
        parking: Parking = baker.make(Parking)

        operation = {
            "name": "Operation 1",
            "parking": str(parking.id),
        }

        response = APIClient().post(
            url,
            {
                "name": operation["name"],
                "parking": operation["parking"],
            },
        )

        assert response.status_code == 201
        assert response.json() == {
            "id": response.json()["id"],
            "name": operation["name"],
            "parking": operation["parking"],
        }

    def test_if_throw_error_with_invalid_parking(self) -> None:
        operation = {
            "name": "Operation 1",
            "parking": str(uuid.uuid4()),
        }

        response = APIClient().post(
            url,
            {
                "name": operation["name"],
                "parking": operation["parking"],
            },
        )

        assert response.status_code == 400
        assert (
            f'Invalid pk "{operation["parking"]}" - object does not exist.'
            in response.json()["parking"][0]
        )

    def test_if_create_a_parking_sector_not_passing_the_parking(
        self,
    ) -> None:
        parking: Parking = baker.make(Parking)

        operation = {
            "name": "Operation 1",
        }

        response = APIClient().post(
            url,
            {
                "name": operation["name"],
            },
        )

        print(response.content)
        assert response.status_code == 400
        assert "This field is required." in response.json()["parking"][0]
