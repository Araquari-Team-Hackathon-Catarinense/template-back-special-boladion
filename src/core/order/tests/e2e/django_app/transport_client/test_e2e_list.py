import json
import uuid

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.order.infra.order_django_app.models import (
    PurchaseSaleOrder,
    TransportContract,
)
from django_project.settings import API_VERSION


@pytest.mark.django_db
class TestTransportContractListAPI:
    def test_list_transport_contracts(self) -> None:
        company = baker.make(Company)
        carrier = baker.make(Company, id=uuid.uuid4())
        purchase_sale_order = baker.make(PurchaseSaleOrder)

        created_contracts = baker.make(
            TransportContract,
            company=company,
            carrier=carrier,
            purchase_sale_order=purchase_sale_order,
            balance=10.0,
            _quantity=3,
        )

        url = f"/api/{API_VERSION}/order/transport-contracts/"
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        response = APIClient().get(url, **headers)

        response_data = response.json()
        print("Response Data:", response_data)

        assert response.status_code == 200
        assert response_data["total"] == 3
        assert len(response_data["results"]) == 3

        for i, contract in enumerate(created_contracts):
            response_contract = response_data["results"][i]
            assert response_contract["company"] == str(contract.company.id)
            assert response_contract["carrier"] == str(contract.carrier.id)
            assert response_contract["purchase_sale_order"] == str(
                contract.purchase_sale_order.id
            )
            assert response_contract["balance"] == contract.balance
