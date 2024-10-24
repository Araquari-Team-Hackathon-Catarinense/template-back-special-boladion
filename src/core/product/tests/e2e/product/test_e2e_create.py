import pytest
from model_bakery import baker
from pycpfcnpj import gen
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company


@pytest.mark.django_db
class TestCreateAPI:
    def test_create_a_valid_product(self) -> None:
        url: str = "/api/products/"
        company = baker.make(Company)
        product = {
            "description": "Product 1",
            "internal_code": "123",
            "company": str(company.id),
        }

        response = APIClient().post(
            url,
            {
                "description": product["description"],
                "internal_code": product["internal_code"],
                "company": product["company"],
            },
        )

        assert response.status_code == 201
        assert response.json()["description"] == product["description"]
        assert response.json()["internal_code"] == product["internal_code"]
        assert response.json()["company"] == product["company"]
        assert "id" in response.json()

    def test_if_throw_error_with_invalid_company(self) -> None:
        url = "/api/products/"
        product = {
            "description": "Product 1",
            "internal_code": "123",
            "company": "112",
        }

        response = APIClient().post(
            url,
            {
                "description": product["description"],
                "internal_code": product["internal_code"],
                "company": product["company"],
            },
        )

        assert response.status_code == 400
        assert "company" in response.json()
        assert "não é um UUID válido" in response.json()["company"][0]

    def test_if_throw_error_with_invalid_is_active(self) -> None:
        url = "/api/products/"
        company = baker.make(Company)
        product = {
            "company": str(company.id),
            "description": "Product 1",
            "internal_code": "123",
            "is_active": "invalid",
        }

        response = APIClient().post(
            url,
            {
                "description": product["description"],
                "internal_code": product["internal_code"],
                "company": product["company"],
                "is_active": product["is_active"],
            },
        )

        assert response.status_code == 400
        assert "is_active" in response.json()
