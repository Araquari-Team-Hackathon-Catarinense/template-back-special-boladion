import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Contract


@pytest.mark.django_db
class TestListAPI:
    def test_list_contracts(self) -> None:
        created_contracts = baker.make(Contract, _quantity=3)

        url = "/api/contracts/"
        response = APIClient().get(url)

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
                        "name": contract.source_company.name
                    },
                    "target_company": {
                        "id": str(contract.target_company.id),
                        "name": contract.target_company.name
                    },
                    "contract_type": contract.contract_type,
                }
                for contract in created_contracts
            ],
        }

        assert response.status_code == 200
        assert len(response.json()["results"]) == 3
        assert response.json() == expected_data
