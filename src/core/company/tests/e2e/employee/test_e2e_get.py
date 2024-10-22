import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Employee


@pytest.mark.django_db
class TestListAPI:
    def test_list_employees(self) -> None:
        created_employees = baker.make(Employee, _quantity=3)

        url = "/api/employees/"
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
                    "id": str(employee.id),
                    "company": str(employee.company.id),
                    "user": employee.user.id,
                    "is_active": employee.is_active,
                }
                for employee in created_employees
            ],
        }

        assert response.status_code == 200
        assert len(response.json()["results"]) == 3
        assert json.loads(response.content) == expected_data
