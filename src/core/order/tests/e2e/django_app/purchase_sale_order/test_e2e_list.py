import json
import uuid

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.order.infra.order_django_app.models import (
    MeasurementUnit,
    Packing,
    PurchaseSaleOrder,
)
from core.product.infra.product_django_app.models import Product


@pytest.mark.django_db
class TestPurchaseSaleOrderListAPI:
    def test_list_purchase_sale_orders(self) -> None:
        company = baker.make(Company)
        client = baker.make(Company, id=uuid.uuid4())
        product = baker.make(Product)
        measurement_unit = baker.make(MeasurementUnit)
        packing = baker.make(Packing)
        operation_terminal = baker.make(Company)
        operation_type = "CARGA"

        created_orders = baker.make(
            PurchaseSaleOrder,
            client=client,
            product=product,
            measurement_unit=measurement_unit,
            packing=packing,
            operation_terminal=operation_terminal,
            operation_type=operation_type,
            company=company,
            quantity=10.0,
            _quantity=3,
        )

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
                    "id": str(order.id),
                    "company": str(order.company.id),
                    "client": str(order.client.id),
                    "product": str(order.product.id),
                    "packing": str(order.packing.id),
                    "measurement_unit": str(order.measurement_unit.description),
                    "quantity": order.quantity,
                    "balance": order.balance,
                    "operation_type": order.operation_type,
                    "operation_terminal": str(order.operation_terminal.id),
                }
                for order in created_orders
            ],
        }

        url = "/api/purchase-sale-orders/"
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        response = APIClient().get(url, **headers)

        assert response.status_code == 200
        assert len(response.json()["results"]) == 3
        assert json.loads(response.content) == expected_data
