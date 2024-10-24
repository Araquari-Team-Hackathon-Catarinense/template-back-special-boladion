import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Contract


@pytest.mark.django_db
class TestPatchAPI:
    def test_patch_a_valid_contract(self) -> None:
        contracts = baker.make(Contract, _quantity=3)

        url = f"/api/contracts/{contracts[0].id}/"

        new_data = {
            "contract_type": "TRANSPORTADORA",
        }

        response = APIClient().patch(url, new_data, format="json")

        expected_data = {
            "id": str(contracts[0].id),
            "source_company":str(contracts[0].source_company.id),
            "target_company": str(contracts[0].target_company.id),
            "contract_type": new_data["contract_type"],
        }

        # breakpoint()
        assert response.status_code == 200
        assert response.json() == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_contract(self) -> None:
        url = "/api/contracts/12345678-1234-1234-1234-123456789012/"
        new_data = {
            "contract_type": "TRANSPORTADORA",
        }
        response = APIClient().patch(url, new_data, format="json")
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Contract matches the given query."
        }
