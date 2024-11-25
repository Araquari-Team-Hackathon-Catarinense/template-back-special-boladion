import pytest
from pycpfcnpj import gen
from rest_framework.test import APIClient

from django_project.settings import API_VERSION


@pytest.mark.django_db
class TestListAPI:
    def test_create_a_valid_company(self) -> None:
        url: str = f"/api/{API_VERSION}/company/companies/"
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
        url = f"/api/{API_VERSION}/company/companies/"
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

        response_data = response.json()
        assert "document_number" in response_data

        errors_list = response_data["document_number"]
        first_error = errors_list[0]
        error_message = first_error.get("document_number", "")

        assert "CNPJ inválido." == error_message

    def test_if_throw_a_error_with_invalid_person_type_and_document_number_size(
        self,
    ) -> None:
        url = f"/api/{API_VERSION}/company/companies/"
        company = {
            "name": "Company 1",
            "trade_name": "Trade Name 1",
            "person_type": "invalid",
            "is_active": True,
            "document_number": "12345678901234",
        }

        response = APIClient().post(
            url,
            company,
        )

        assert response.status_code == 400

        response_data = response.json()

        # Verifica o erro em 'person_type'
        assert "person_type" in response_data
        assert (
            f'"{company["person_type"]}" não é um escolha válido.'
            in response_data["person_type"]
        )

        # Verifica o erro em 'document_number'
        assert "document_number" in response_data

        document_number_errors = response_data["document_number"]
        first_error = document_number_errors[0]
        error_message = first_error.get("document_number", "")

        assert error_message == "CPF/CNPJ inválido."
