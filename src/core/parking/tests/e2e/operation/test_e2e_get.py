import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.parking.infra.parking_django_app.models import Operation, Parking

url = "/api/operations/"


@pytest.mark.django_db
class TestOperationListAPI:
    def test_list_operation(self) -> None:
        parking: Parking = baker.make(Parking)
        created_operation = baker.make(Operation, _quantity=3, parking=parking)

        response = APIClient().get(url)

        expected_data = {
            "total": 3,
            "num_pages": 1,
            "page_number": 1,
            "page_size": 20,
            "links": {
                "next": None,
                "previous": None,
            },
            "results": [
                {
                    "id": str(operation.id),
                    "name": operation.name,
                }
                for operation in created_operation
            ],
        }

        print(response.json())
        assert response.status_code == 200
        assert len(response.json()["results"]) == 3
        assert json.loads(response.content) == expected_data
