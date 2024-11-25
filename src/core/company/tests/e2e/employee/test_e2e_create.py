import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.user.infra.user_django_app.models import User
from django_project.settings import API_VERSION


@pytest.mark.django_db
class TestCreateAPI:
    def test_create_a_valid_employee(self) -> None:

        company = baker.make(Company)
        user = baker.make(User)
        employee = {
            "company": str(company.id),
            "user": str(user.id),
            "is_active": True,
        }
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        url: str = f"/api/{API_VERSION}/company/employees/"
        response = APIClient().post(
            url,
            {
                "company": employee["company"],
                "user": employee["user"],
                "is_active": employee["is_active"],
            },
            **headers,
        )

        assert response.status_code == 201
        assert str(response.json()["user"]) == employee["user"]
        assert response.json()["is_active"] == employee["is_active"]
        assert "id" in response.json()

    def test_if_throw_error_with_invalid_company(self) -> None:
        user = baker.make(User)
        company = baker.make(Company)
        company.id = 123
        employee = {
            "company": str(company.id),
            "user": str(user.id),
            "is_active": True,
        }
        url = f"/api/{API_VERSION}/company/employees/"
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}

        response = APIClient().post(
            url,
            {
                "company": employee["company"],
                "user": employee["user"],
                "is_active": employee["is_active"],
            },
            **headers,
        )

        assert response.status_code == 400
        assert "company" in response.json()
        assert "O valor “123” não é um UUID válido" in response.json()["company"][0]

    def test_if_throw_error_with_invalid_user_id(self) -> None:
        url = f"/api/{API_VERSION}/company/employees/"
        company = baker.make(Company)
        employee = {
            "company": str(company.id),
            "user": 123,
            "is_active": True,
        }
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        response = APIClient().post(
            url,
            {
                "company": employee["company"],
                "user": employee["user"],
                "is_active": employee["is_active"],
            },
            **headers,
        )

        assert response.status_code == 400
        assert "user" in response.json()
        assert "não é um UUID válido" in response.json()["user"][0]

    def test_if_throw_error_with_invalid_is_active(self) -> None:
        url = f"/api/{API_VERSION}/company/employees/"
        company = baker.make(Company)
        user = baker.make(User)
        employee = {
            "company": str(company.id),
            "user": str(user.id),
            "is_active": "invalid",
        }
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        response = APIClient().post(
            url,
            {
                "company": employee["company"],
                "user": employee["user"],
                "is_active": employee["is_active"],
            },
            **headers,
        )

        assert response.status_code == 400
        assert "is_active" in response.json()
