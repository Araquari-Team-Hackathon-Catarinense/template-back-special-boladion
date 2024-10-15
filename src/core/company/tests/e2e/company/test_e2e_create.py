import pytest
from rest_framework.test import APIClient

from core.company.infra.django_app.models import Company


@pytest.mark.django_db
class TestListAPI:
    def test_create_a_valid_category(self) -> None:
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

        assert response.status_code == 201

    def test_if_throw_a_error_with_invalid_person_type(self) -> None:
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
            f'"{company["person_type"]}" is not a valid choice.'
            in response.json()["person_type"][0]
        )
