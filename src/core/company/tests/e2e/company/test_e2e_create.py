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

    def test_if_a_new_uuid_is_generated_with_more_companies(self) -> None:
        companies = [
            {
                "name": "Company 1",
                "trade_name": "Trade Name 1",
                "person_type": "PJ",
                "is_active": True,
                "document_number": "12345678901234",
            },
            {
                "name": "Company 2",
                "trade_name": "Trade Name 2",
                "person_type": "PF",
                "is_active": True,
                "document_number": "12345678911",
            },
        ]

        url = "/api/companies/"
        response1 = APIClient().post(
            url,
            {
                "name": companies[0]["name"],
                "trade_name": companies[0]["trade_name"],
                "person_type": companies[0]["person_type"],
                "is_active": companies[0]["is_active"],
                "document_number": companies[0]["document_number"],
            },
        )
        response2 = APIClient().post(
            url,
            {
                "name": companies[1]["name"],
                "trade_name": companies[1]["trade_name"],
                "person_type": companies[1]["person_type"],
                "is_active": companies[1]["is_active"],
                "document_number": companies[1]["document_number"],
            },
        )

        assert response1.status_code == 201
        assert response2.status_code == 201
