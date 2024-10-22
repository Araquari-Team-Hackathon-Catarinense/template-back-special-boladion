import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company


@pytest.mark.django_db
class TestPatchCompanyAPI:
    def test_patch_a_valid_company(self) -> None:
        companies = baker.make(Company, _quantity=3)

        url = f"/api/companies/{companies[0].id}/"

        new_data = {
            "trade_name": "New Trade Name",
            "is_active": False,
            "address": {
                "street": "New Street",
                "number": 123,
                "complement": "New Complement",
                "zip_code": "12345-678",
                "city": "New City",
                "state": "New State",
                "country": "New Country",
            },
        }

        response = APIClient().patch(url, new_data, format="json")

        expected_data = {
            "id": str(companies[0].id),
            "name": companies[0].name,
            "trade_name": new_data["trade_name"],
            "person_type": companies[0].person_type,
            "document_number": companies[0].document_number,
            "is_active": new_data["is_active"],
            "address": new_data["address"],
            "contacts": companies[0].contacts,
            "system_admin": companies[0].system_admin,
        }
        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_company(self) -> None:
        url = "/api/companies/12345678-1234-1234-1234-123456789012/"
        new_data = {
            "trade_name": "New Trade Name",
            "is_active": False,
            "address": {
                "street": "New Street",
                "number": 123,
                "complement": "New Complement",
                "zip_code": "12345-678",
                "city": "New City",
                "state": "New State",
                "country": "New Country",
            },
        }
        response = APIClient().patch(url, new_data, format="json")
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Company matches the given query."
        }
