import unittest
import uuid

import pytest
from django.db import models
from model_bakery import baker

from core.company.infra.company_django_app.models import Company
from core.order.infra.order_django_app.models import (
    MeasurementUnit,
    Packing,
    PurchaseSaleOrder,
)
from core.product.infra.product_django_app.models import Product


@pytest.mark.django_db()
class PurchaseSaleOrderUnitModelInt(unittest.TestCase):

    def test_mapping(self):
        table_name = PurchaseSaleOrder._meta.db_table
        self.assertEqual(table_name, "purchase_sale_order")

        fields_name = tuple(field.name for field in PurchaseSaleOrder._meta.fields)
        self.assertEqual(
            fields_name,
            (
                "deleted_at",
                "deleted_by_cascade",
                "created_at",
                "updated_at",
                "id",
                "company",
                "client",
                "product",
                "measurement_unit",
                "packing",
                "operation_terminal",
                "quantity",
                "balance",
                "operation_type",
            ),
        )

        id_field: models.UUIDField = PurchaseSaleOrder.id.field
        self.assertIsInstance(id_field, models.UUIDField)
        self.assertTrue(id_field.primary_key)
        self.assertFalse(id_field.editable)

        company_field: models.ForeignKey = PurchaseSaleOrder.company.field
        self.assertIsInstance(company_field, models.ForeignKey)
        self.assertFalse(company_field.blank)
        self.assertFalse(company_field.null)

        client_field: models.ForeignKey = PurchaseSaleOrder.client.field
        self.assertIsInstance(client_field, models.ForeignKey)
        self.assertFalse(client_field.blank)
        self.assertFalse(client_field.null)

        product_field: models.ForeignKey = PurchaseSaleOrder.product.field
        self.assertIsInstance(product_field, models.ForeignKey)
        self.assertFalse(product_field.blank)
        self.assertFalse(product_field.null)

        measurement_unit_field: models.ForeignKey = (
            PurchaseSaleOrder.measurement_unit.field
        )
        self.assertIsInstance(measurement_unit_field, models.ForeignKey)
        self.assertTrue(measurement_unit_field.blank)
        self.assertTrue(measurement_unit_field.null)

        packing_field: models.ForeignKey = PurchaseSaleOrder.packing.field
        self.assertIsInstance(packing_field, models.ForeignKey)
        self.assertTrue(packing_field.blank)
        self.assertTrue(packing_field.null)

        quantity_field: models.FloatField = PurchaseSaleOrder.quantity.field
        self.assertIsInstance(quantity_field, models.FloatField)
        self.assertTrue(quantity_field.blank)
        self.assertTrue(quantity_field.null)

        balance_field: models.FloatField = PurchaseSaleOrder.balance.field
        self.assertIsInstance(balance_field, models.FloatField)
        self.assertTrue(balance_field.blank)
        self.assertTrue(balance_field.null)

        operation_terminal_field: models.ForeignKey = (
            PurchaseSaleOrder.operation_terminal.field
        )
        self.assertIsInstance(operation_terminal_field, models.ForeignKey)
        self.assertFalse(operation_terminal_field.blank)
        self.assertFalse(operation_terminal_field.null)

        operation_type_field: models.CharField = PurchaseSaleOrder.operation_type.field
        self.assertIsInstance(operation_type_field, models.CharField)
        self.assertEqual(operation_type_field.max_length, 255)
        self.assertTrue(operation_type_field.choices)

    def test_create(self):
        company = baker.make(Company)
        client = baker.make(Company)
        product = baker.make(Product)
        measurement_unit = baker.make(MeasurementUnit)
        packing = baker.make(Packing)
        operation_terminal = baker.make(Company)
        id = uuid.uuid4()

        arrange = {
            "id": id,
            "company": company,
            "client": client,
            "product": product,
            "measurement_unit": measurement_unit,
            "packing": packing,
            "quantity": 10.5,
            "balance": 10.5,
            "operation_terminal": operation_terminal,
            "operation_type": "purchase",
        }

        purchase_sale_order = PurchaseSaleOrder.objects.create(
            id=arrange["id"],
            company=arrange["company"],
            client=arrange["client"],
            product=arrange["product"],
            measurement_unit=arrange["measurement_unit"],
            packing=arrange["packing"],
            quantity=arrange["quantity"],
            balance=arrange["balance"],
            operation_terminal=arrange["operation_terminal"],
            operation_type=arrange["operation_type"],
        )

        self.assertEqual(purchase_sale_order.id, arrange["id"])
        self.assertEqual(purchase_sale_order.company, arrange["company"])
        self.assertEqual(purchase_sale_order.client, arrange["client"])
        self.assertEqual(purchase_sale_order.product, arrange["product"])
        self.assertEqual(
            purchase_sale_order.measurement_unit, arrange["measurement_unit"]
        )
        self.assertEqual(purchase_sale_order.packing, arrange["packing"])
        self.assertEqual(purchase_sale_order.quantity, arrange["quantity"])
        self.assertEqual(purchase_sale_order.balance, arrange["balance"])
        self.assertEqual(
            purchase_sale_order.operation_terminal, arrange["operation_terminal"]
        )
        self.assertEqual(purchase_sale_order.operation_type, arrange["operation_type"])
