import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company, Contract
from django_project.settings import API_VERSION


@pytest.mark.django_db
class TestListAPI:
    def test_list_contracts(self) -> None:
        company = baker.make(Company)
        created_contracts = baker.make(Contract, _quantity=3, source_company=company)

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
                        "avatar": (
                            f"http://localhost:8000{contract.source_company.avatar.url}"
                            if contract.source_company.avatar
                            else None
                        ),
                    },
                    "target_company": {
                        "id": str(contract.target_company.id),
                        "name": contract.target_company.name,
                        "avatar": (
                            f"http://localhost:8000{contract.target_company.avatar.url}"
                            if contract.target_company.avatar
                            else None
                        ),
                    },
                    "contract_type": contract.contract_type,
                }
                for contract in created_contracts
            ],
        }

        url = f"/api/{API_VERSION}/company/contracts/"
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        response = APIClient().get(url, **headers)
        print(
            json.dumps(response.json(), indent=2)
        )  # Verifique a estrutura da resposta

        assert response.status_code == 200
        assert len(response.json()["results"]) == 3

        # Comparar apenas os campos necessários
        response_data = response.json()
        for i, contract in enumerate(created_contracts):
            response_contract = response_data["results"][i]
            assert response_contract["id"] == str(contract.id)
            assert response_contract["source_company"]["id"] == str(
                contract.source_company.id
            )
            assert (
                response_contract["source_company"]["name"]
                == contract.source_company.name
            )
            assert response_contract["source_company"]["avatar"] == (
                f"http://localhost:8000{contract.source_company.avatar.url}"
                if contract.source_company.avatar
                else None
            )
            assert response_contract["target_company"]["id"] == str(
                contract.target_company.id
            )
            assert (
                response_contract["target_company"]["name"]
                == contract.target_company.name
            )
            assert response_contract["target_company"]["avatar"] == (
                f"http://localhost:8000{contract.target_company.avatar.url}"
                if contract.target_company.avatar
                else None
            )
            assert response_contract["contract_type"] == contract.contract_type
