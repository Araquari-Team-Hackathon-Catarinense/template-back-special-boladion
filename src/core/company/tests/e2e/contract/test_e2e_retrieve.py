import json
from wsgiref import headers

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Contract


@pytest.mark.django_db
class TestRetrieveAPI:
    def test_retrieve_a_valid_contract(self) -> None:
        contracts = baker.make(Contract, _quantity=3)

        company = contracts[0].source_company
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        url = f"/api/contracts/{contracts[0].id}/"
        response = APIClient().get(url, **headers)

        expected_data = {
            "id": str(contracts[0].id),
            "source_company": {
                "id": str(contracts[0].source_company.id),
                "name": contracts[0].source_company.name,
            },
            "target_company": {
                "id": str(contracts[0].target_company.id),
                "name": contracts[0].target_company.name,
            },
            "contract_type": contracts[0].contract_type,
        }
        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_contract(self) -> None:
        contracts = baker.make(Contract, _quantity=3)
        company = contracts[0].source_company

        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        url = "/api/contracts/12345678-1234-1234-1234-123456789012/"

        response = APIClient().get(url, **headers)
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Contract matches the given query."
        }
