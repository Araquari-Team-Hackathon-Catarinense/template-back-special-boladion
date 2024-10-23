import pytest
from model_bakery import baker
from pycpfcnpj import gen
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.user.infra.user_django_app.models import User


@pytest.mark.django_db
class TestCreateAPI:
    def test_create_a_valid_contracts(self) -> None:
        url: str = "/api/contracts/"
        companies = baker.make(Company, _quantity=2)

        response = APIClient().post(
            url,
            {
                "source_company": str(companies[0].id),
                "target_company": str(companies[1].id),
                "contract_type": "CLIENTE",
            },
        )

        assert response.status_code == 201
        assert str(response.json()["source_company"]) == str(companies[0].id)
        assert str(response.json()["target_company"]) == str(companies[1].id)
        assert response.json()["contract_type"] == "CLIENTE"
        assert "id" in response.json()

    def test_if_throw_error_with_invalid_target_company(self) -> None:
        url = "/api/contracts/"
        company = baker.make(Company)

        response = APIClient().post(
            url,
            {
                "source_company": str(company.id),
                "target_company": 123,
                "contract_type": "CLIENTE",
            },
        )

        assert response.status_code == 400
        assert "target_company" in response.json()
        assert "O valor “123” não é um UUID válido" in response.json()["target_company"][0]


    def test_if_throw_error_with_invalid_contract_type(self) -> None:
        url = "/api/contracts/"
        company = baker.make(Company)
        user = baker.make(User)

        response = APIClient().post(
              url,
            {
                "source_company": str(company.id),
                "target_company": str(company.id),
                "contract_type": "invalid",
            },
        )

        assert response.status_code == 400
        assert "contract_type" in response.json()
