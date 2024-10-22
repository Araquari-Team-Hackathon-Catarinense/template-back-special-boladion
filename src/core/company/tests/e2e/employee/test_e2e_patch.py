import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company, Employee


@pytest.mark.django_db
class TestPatchAPI:
    def test_patch_a_valid_employee(self) -> None:
        employees = baker.make(Employee, _quantity=3)

        url = f"/api/employees/{employees[0].id}/"

        new_data = {
            "is_active": False,
        }

        response = APIClient().patch(url, new_data, format="json")

        expected_data = {
            "id": str(employees[0].id),
            "company": str(employees[0].company.id),
            "user": employees[0].user.id,
            "is_active": new_data["is_active"],
        }

        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_employee(self) -> None:
        url = "/api/employees/12345678-1234-1234-1234-123456789012/"
        new_data = {
            "is_active": False,
        }
        response = APIClient().patch(url, new_data, format="json")
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Employee matches the given query."
        }
