import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import Operation, Parking

url = "/api/operations/"


@pytest.mark.django_db
class TestOperationListAPI:
    def test_list_operation(self) -> None:
        company: Company = baker.make(Company)
        parking: Parking = baker.make(Parking, company=company)
        created_operations = baker.make(Operation, _quantity=3, parking=parking)

        url = "/api/operations/"

        headers = {"HTTP_X_COMPANY_ID": str(company.id)}

        response = APIClient().get(url, **headers)

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
                    "parking": parking.description,
                }
                for operation in created_operations
            ],
        }

        assert response.status_code == 200
        assert len(response.json()["results"]) == 3
        assert response.json() == expected_data
