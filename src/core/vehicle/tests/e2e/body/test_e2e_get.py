import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.vehicle.infra.vehicle_django_app.models import Body

url = "/api/bodies/"


@pytest.mark.django_db
class TestBodyListAPI:
    def test_list_body(self) -> None:
        created_bodies = baker.make(Body, _quantity=3)

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
                    "id": str(body.id),
                    "description": body.description,
                }
                for body in created_bodies
            ],
        }

        assert response.status_code == 200
        assert len(response.json()["results"]) == 3
        assert json.loads(response.content) == expected_data
