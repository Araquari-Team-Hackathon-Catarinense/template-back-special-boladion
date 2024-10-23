import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Employee


@pytest.mark.django_db
class TestRetrieveAPI:
    def test_retrieve_a_valid_employee(self) -> None:
        employees = baker.make(Employee, _quantity=3)

        url = f"/api/employees/{employees[0].id}/"
        response = APIClient().get(url)

        expected_data = {
            "id": str(employees[0].id),
            "company": str(employees[0].company.id),
            "user": str(employees[0].user.id),
            "is_active": employees[0].is_active,
        }
        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_employee(self) -> None:
        url = "/api/employees/12345678-1234-1234-1234-123456789012/"
        response = APIClient().get(url)
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Employee matches the given query."
        }
