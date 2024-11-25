import pytest
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company, Contract
from core.order.infra.order_django_app.models import PurchaseSaleOrder
from django_project.settings import API_VERSION

url = f"/api/{API_VERSION}/order/transport-contracts/"


@pytest.mark.django_db
class TestCreateTransportContractAPITest:
    def test_create_valid_transport_contract(self):
        company = baker.make(Company)
        carrier = baker.make(Company)

        baker.make(
            Contract,
            source_company=company,
            target_company=carrier,
            contract_type="TRANSPORTADORA",
        )
        purchase_sale_order = baker.make(PurchaseSaleOrder, company=company)

        operation_data = {
            "company": str(company.id),
            "carrier": str(carrier.id),
            "purchase_sale_order": str(purchase_sale_order.id),
            "quantity": 10.0,
            "balance": 100.0,
        }

        headers = {"HTTP_X_COMPANY_ID": str(company.id)}

        response = APIClient().post(
            url,
            operation_data,
            format="json",
            **headers,
        )
        print("Response Data (Error Case):", response.json())

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["company"] == operation_data["company"]
        assert response.json()["carrier"] == operation_data["carrier"]
        assert (
            response.json()["purchase_sale_order"]
            == operation_data["purchase_sale_order"]
        )

    def test_create_invalid_transport_contract_missing_contract(self):
        company = baker.make(Company)
        carrier = baker.make(Company)

        # baker.make(
        #     Contract,
        #     source_company=company,
        #     target_company=carrier,
        #     contract_type="TRANSPORTADORA",
        # )

        purchase_sale_order = baker.make(PurchaseSaleOrder, company=company)

        operation_data = {
            "company": str(company.id),
            "carrier": str(carrier.id),
            "purchase_sale_order": str(purchase_sale_order.id),
            "quantity": 10.0,
            "balance": 10.0,
        }
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        response = APIClient().post(
            url,
            operation_data,
            format="json",
            **headers,
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert (
            "A transportadora deve ser uma empresa com um contrato do tipo TRANSPORTADORA com a empresa fornecedora."
            in str(response.data)
        )
