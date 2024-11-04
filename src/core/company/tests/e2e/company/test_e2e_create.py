import pytest
from pycpfcnpj import gen
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company


@pytest.mark.django_db
class TestListAPI:
    def test_create_a_valid_company(self) -> None:
        url: str = "/api/companies/"
        cnpj: str = gen.cnpj()
        company = {
            "name": "Company 1",
            "trade_name": "Trade Name 1",
            "person_type": "PJ",
            "is_active": True,
            "document_number": cnpj,
        }

        response = APIClient().post(
            url,
            {
                "name": company["name"],
                "trade_name": company["trade_name"],
                "person_type": company["person_type"],
                "is_active": company["is_active"],
                "document_number": company["document_number"],
            },
        )

        assert response.status_code == 201
        assert response.json()["name"] == company["name"]
        assert response.json()["trade_name"] == company["trade_name"]
        assert response.json()["person_type"] == company["person_type"]
        assert response.json()["document_number"] == company["document_number"]
        assert response.json()["is_active"] == company["is_active"]
        assert "id" in response.json()

    def test_if_throw_error_with_invalid_document_number(self) -> None:
        url = "/api/companies/"
        company = {
            "name": "Company 1",
            "trade_name": "Trade Name 1",
            "person_type": "PJ",
            "is_active": True,
            "document_number": "12345678901234",
        }

        response = APIClient().post(
            url,
            {
                "name": company["name"],
                "trade_name": company["trade_name"],
                "person_type": company["person_type"],
                "is_active": company["is_active"],
                "document_number": company["document_number"],
            },
        )

        assert response.status_code == 400
        assert "document_number" in response.json()
        assert "CNPJ inválido." in response.json()["document_number"][0]

    def test_if_throw_a_error_with_invalid_person_type_and_document_number_size(
        self,
    ) -> None:
        url = "/api/companies/"
        company = {
            "name": "Company 1",
            "trade_name": "Trade Name 1",
            "person_type": "invalid",
            "is_active": True,
            "document_number": "12345678901234",
        }

        response = APIClient().post(
            url,
            {
                "name": company["name"],
                "trade_name": company["trade_name"],
                "person_type": company["person_type"],
                "is_active": company["is_active"],
                "document_number": company["document_number"],
            },
        )

        assert response.status_code == 400
        assert "person_type" in response.json()
        assert (
            f'"{company["person_type"]}" não é um escolha válido.'
            in response.json()["person_type"][0]
        )
        assert "document_number" in response.json()
        assert "Documento inválido." in response.json()["document_number"][0]
