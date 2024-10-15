import json
from model_bakery import baker
import pytest
from rest_framework.test import APIClient

from core.company.infra.django_app.models import Company


@pytest.mark.django_db
class TestRetrieveCompanyAPI:
    def test_retrieve_a_valid_company(self) -> None:
        companies = baker.make(Company, _quantity=3)

        url = f"/api/companies/{companies[0].id}/"
        response = APIClient().get(url)

        expected_data = {
            "id": str(companies[0].id),
            "name": companies[0].name,
            "trade_name": companies[0].trade_name,
            "person_type": companies[0].person_type,
            "document_number": companies[0].document_number,
            "is_active": companies[0].is_active,
            "address": companies[0].address,
            "contacts": companies[0].contacts,
            "system_admin": companies[0].system_admin,
        }
        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_company(self) -> None:
        url = "/api/companies/12345678-1234-1234-1234-123456789012/"
        response = APIClient().get(url)
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Company matches the given query."
        }
