import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company, Employee
from django_project.settings import API_VERSION


@pytest.mark.django_db
class TestRetrieveAPI:
    def test_retrieve_a_valid_employee(self) -> None:
        company = baker.make(Company)
        employees = baker.make(Employee, company=company, _quantity=3)
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        url = f"/api/{API_VERSION}/company/employees/{employees[0].id}/"
        response = APIClient().get(url, **headers)

        expected_data = {
            "id": str(employees[0].id),
            "company": str(employees[0].company.name),
            "user": {
                "name": employees[0].user.name,
                "email": employees[0].user.email,
            },
            "is_active": employees[0].is_active,
        }
        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_employee(self) -> None:
        company = baker.make(Company)

        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        url = f"/api/{API_VERSION}/company/employees/12345678-1234-1234-1234-123456789012/"
        response = APIClient().get(url, **headers)
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Employee matches the given query."
        }
