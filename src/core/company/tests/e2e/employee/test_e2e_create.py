import pytest
from model_bakery import baker
from pycpfcnpj import gen
from rest_framework.test import APIClient

from core.company.infra.django_app.models import Company
from core.user.infra.user_django_app.models import User


@pytest.mark.django_db
class TestCreateAPI:
    def test_create_a_valid_employee(self) -> None:
        url: str = "/api/employees/"
        company = baker.make(Company)
        user = baker.make(User)
        employee = {
            "company_id": str(company.id),
            "user_id": str(user.id),
            "is_active": True,
        }

        response = APIClient().post(
            url,
            {
                "company_id": employee["company_id"],
                "user_id": employee["user_id"],
                "is_active": employee["is_active"],
            },
        )

        assert response.status_code == 201
        assert str(response.json()["company_id"]) == employee["company_id"]
        assert str(response.json()["user_id"]) == employee["user_id"]
        assert response.json()["is_active"] == employee["is_active"]
        assert "id" in response.json()

    def test_if_throw_error_with_invalid_company_id(self) -> None:
        url = "/api/employees/"
        user = baker.make(User)
        employee = {
            "company_id": "123",
            "user_id": str(user.id),
            "is_active": True,
        }

        response = APIClient().post(
            url,
            {
                "company_id": employee["company_id"],
                "user_id": employee["user_id"],
                "is_active": employee["is_active"],
            },
        )

        assert response.status_code == 400
        assert "company_id" in response.json()
        assert "O valor “123” não é um UUID válido" in response.json()["company_id"][0]

    def test_if_throw_error_with_invalid_user_id(self) -> None:
        url = "/api/employees/"
        company = baker.make(Company)
        employee = {
            "company_id": str(company.id),
            "user_id": "123",
            "is_active": True,
        }

        response = APIClient().post(
            url,
            {
                "company_id": employee["company_id"],
                "user_id": employee["user_id"],
                "is_active": employee["is_active"],
            },
        )

        assert response.status_code == 400
        assert "user_id" in response.json()
        assert 'Pk inválido "123" - objeto não existe.' in response.json()["user_id"][0]

    def test_if_throw_error_with_invalid_is_active(self) -> None:
        url = "/api/employees/"
        company = baker.make(Company)
        user = baker.make(User)
        employee = {
            "company_id": str(company.id),
            "user_id": str(user.id),
            "is_active": "invalid",
        }

        response = APIClient().post(
            url,
            {
                "company_id": employee["company_id"],
                "user_id": employee["user_id"],
                "is_active": employee["is_active"],
            },
        )

        assert response.status_code == 400
        assert "is_active" in response.json()
