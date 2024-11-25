import pytest
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company, Contract
from core.order.infra.order_django_app.models import MeasurementUnit, Packing
from core.product.infra.product_django_app.models import Product
from django_project.settings import API_VERSION

url = f"/api/{API_VERSION}/order/purchase-sale-orders/"


@pytest.mark.django_db
class TestCreatePurchaseSaleOrderAPITest:
    def test_create_valid_purchase_sale_order(self):
        company = baker.make(Company)
        client = baker.make(Company)
        product = baker.make(Product)
        measurement_unit = baker.make(MeasurementUnit)

        packing = baker.make(Packing)
        operation_terminal = baker.make(Company)

        baker.make(
            Contract,
            source_company=company,
            target_company=client,
            contract_type="CLIENTE",
        )
        baker.make(
            Contract,
            contract_type="TERMINAL",
            target_company=operation_terminal,
            source_company=company,
        )

        operation_data = {
            "company": str(company.id),
            "client": str(client.id),
            "product": str(product.id),
            "measurement_unit": str(measurement_unit.id),
            "packing": str(packing.id),
            "quantity": 10.0,
            "balance": 100.0,
            "operation_terminal": str(operation_terminal.id),
            "operation_type": "CARGA",
        }

        response = APIClient().post(
            f"/api/{API_VERSION}/order/purchase-sale-orders/",
            operation_data,
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["client"] == operation_data["client"]
        assert (
            response.json()["operation_terminal"]
            == operation_data["operation_terminal"]
        )

    def test_create_invalid_purchase_sale_order_missing_contract(self):
        company = baker.make(Company)
        client = baker.make(Company)
        product = baker.make(Product)
        measurement_unit = baker.make(MeasurementUnit)
        packing = baker.make(Packing)
        operation_terminal = baker.make(Company)

        operation_data = {
            "company": str(company.id),
            "client": str(client.id),
            "product": str(product.id),
            "measurement_unit": str(measurement_unit.id),
            "packing": str(packing.id),
            "quantity": 10.0,
            "balance": 100.0,
            "operation_terminal": str(operation_terminal.id),
            "operation_type": "DESCARGA",
        }
        response = APIClient().post(
            f"/api/{API_VERSION}/order/purchase-sale-orders/",
            operation_data,
            format="json",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert (
            "O cliente deve ser uma empresa com um contrato do tipo CLIENTE com a empresa fornecedora."
            in str(response.data)
        )
