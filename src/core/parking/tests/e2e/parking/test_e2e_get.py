import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import Parking


@pytest.mark.django_db
class TestListAPI:
    def test_list_parkings(self) -> None:
        company: Company = baker.make(Company)
        created_parkings = baker.make(Parking, _quantity=3, entity=company, slots=0)

        url = "/api/parkings/"
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
                    "id": str(parking.id),
                    "description": parking.description,
                    "slots": parking.slots,
                    "entity": str(parking.entity.id),
                }
                for parking in created_parkings
            ],
        }

        print(response.json())
        assert response.status_code == 200
        assert len(response.json()["results"]) == 3
        assert json.loads(response.content) == expected_data
