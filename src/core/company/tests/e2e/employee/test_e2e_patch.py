import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company, Employee
from django_project.settings import API_VERSION


@pytest.mark.django_db
class TestPatchAPI:
    def test_patch_a_valid_employee(self) -> None:
        company = baker.make(Company)
        employees = baker.make(Employee, company=company, _quantity=3)
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        url = f"/api/{API_VERSION}/company/employees/{employees[0].id}/"

        new_data = {
            "is_active": False,
        }

        response = APIClient().patch(url, new_data, format="json", **headers)

        expected_data = {
            "id": str(employees[0].id),
            "user": str(employees[0].user.id),
            "is_active": new_data["is_active"],
        }

        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_employee(self) -> None:
        company = baker.make(Company)
        url = f"/api/{API_VERSION}/company/employees/12345678-1234-1234-1234-123456789012/"
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        new_data = {
            "is_active": False,
        }
        response = APIClient().patch(url, new_data, format="json", **headers)
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Employee matches the given query."
        }
