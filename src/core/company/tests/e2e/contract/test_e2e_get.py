import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company, Contract


@pytest.mark.django_db
class TestListAPI:
    def test_list_contracts(self) -> None:
        company = baker.make(Company)
        created_contracts = baker.make(Contract, _quantity=3, source_company=company)
        # source_company = created_contracts[0].source_company

        expected_data = {
            "total": 3,
            "num_pages": 1,
            "page_number": 1,
            "page_size": 20,
            "links": {
                "next": None,
                "previous": None,
            },
            "results": [
                {
                    "id": str(contract.id),
                    "source_company": {
                        "id": str(contract.source_company.id),
                        "name": contract.source_company.name,
                    },
                    "target_company": {
                        "id": str(contract.target_company.id),
                        "name": contract.target_company.name,
                    },
                    "contract_type": contract.contract_type,
                }
                for contract in created_contracts
            ],
        }
        url = "/api/contracts/"
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        response = APIClient().get(url, **headers)

        assert response.status_code == 200
        assert len(response.json()["results"]) == 3
        assert response.json() == expected_data
