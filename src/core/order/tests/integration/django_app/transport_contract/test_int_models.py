import unittest
import uuid

import pytest
from django.db import models
from model_bakery import baker

from core.company.infra.company_django_app.models import Company
from core.order.infra.order_django_app.models import (
    PurchaseSaleOrder,
    TransportContract,
)


@pytest.mark.django_db()
class TestTransportContractUnitModelInt(unittest.TestCase):
    def test_mapping(self):
        table_name = TransportContract._meta.db_table
        assert table_name == "order_django_app_transportcontract"

        fields_name = tuple(field.name for field in TransportContract._meta.fields)
        assert fields_name == (
            "deleted_at",
            "deleted_by_cascade",
            "created_at",
            "updated_at",
            "id",
            "company",
            "carrier",
            "purchase_sale_order",
            "quantity",
            "balance",
        )

        id_field = TransportContract.id.field
        assert isinstance(id_field, models.UUIDField)
        assert id_field.primary_key is True
        assert id_field.editable is False

        company_field = TransportContract.company.field
        assert isinstance(company_field, models.ForeignKey)

        carrier_field = TransportContract.carrier.field
        assert isinstance(carrier_field, models.ForeignKey)

        purchase_sale_order_field = TransportContract.purchase_sale_order.field
        assert isinstance(purchase_sale_order_field, models.ForeignKey)

        quantity_field = TransportContract.quantity.field
        assert isinstance(quantity_field, models.FloatField)
        assert quantity_field.blank is True
        assert quantity_field.null is True

        balance_field = TransportContract.balance.field
        assert isinstance(balance_field, models.FloatField)
        assert balance_field.blank is True
        assert balance_field.null is True

    def test_create(self):
        company = baker.make(Company)
        carrier = baker.make(Company)
        purchase_sale_order = baker.make(PurchaseSaleOrder)
        id = uuid.uuid4()
        arrange = {
            "id": id,
            "company": company,
            "carrier": carrier,
            "purchase_sale_order": purchase_sale_order,
            "quantity": 10.0,
            "balance": 10.0,
        }
        transport_contract__unit = TransportContract.objects.create(
            id=arrange["id"],
            company=arrange["company"],
            carrier=arrange["carrier"],
            purchase_sale_order=arrange["purchase_sale_order"],
            quantity=arrange["quantity"],
            balance=arrange["balance"],
        )

        self.assertEqual(transport_contract__unit.id, arrange["id"])
