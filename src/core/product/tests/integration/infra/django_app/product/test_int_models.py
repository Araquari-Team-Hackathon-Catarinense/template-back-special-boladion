# pylint: disable=no-member,protected-access
import unittest
from calendar import c

import pytest
from django.db import models
from model_bakery import baker

from core.company.infra.company_django_app.models import Company
from core.product.infra.product_django_app.models import Product


@pytest.mark.django_db()
class TestProductModelInt(unittest.TestCase):

    def test_mapping(self):
        table_name = Product._meta.db_table
        self.assertEqual(table_name, "product")

        fields_name = tuple(field.name for field in Product._meta.fields)
        self.assertEqual(
            fields_name,
            (
                "deleted_at",
                "deleted_by_cascade",
                "created_at",
                "updated_at",
                "id",
                "description",
                "internal_code",
                "is_active",
                "company",
            ),
        )

        id_field: models.UUIDField = Product.id.field
        self.assertIsInstance(id_field, models.UUIDField)
        self.assertTrue(id_field.primary_key)

        description_field: models.CharField = Product.description.field
        self.assertIsInstance(description_field, models.CharField)
        self.assertFalse(description_field.blank)
        self.assertFalse(description_field.null)
        self.assertEqual(description_field.max_length, 200)

        internal_code_field: models.CharField = Product.internal_code.field
        self.assertIsInstance(internal_code_field, models.CharField)
        self.assertFalse(internal_code_field.blank)
        self.assertFalse(internal_code_field.null)
        self.assertEqual(internal_code_field.max_length, 45)

        is_active_field: models.BooleanField = Product.is_active.field
        self.assertIsInstance(is_active_field, models.BooleanField)
        self.assertTrue(is_active_field.default)

        company_field: models.ForeignKey = Product.company.field
        self.assertIsInstance(company_field, models.ForeignKey)
        self.assertFalse(company_field.blank)
        self.assertFalse(company_field.null)

        created_at_field: models.DateTimeField = Product.created_at.field
        self.assertIsInstance(created_at_field, models.DateTimeField)

        updated_at_field: models.DateTimeField = Product.updated_at.field
        self.assertIsInstance(updated_at_field, models.DateTimeField)

    def test_create(self):
        company = baker.make(Company)
        arrange = {
            "id": "af46842e-027d-4c91-b259-3a3642144ba4",
            "description": "Product 1",
            "internal_code": "123",
            "is_active": True,
            "company": company,
        }

        product = Product.objects.create(**arrange)

        self.assertEqual(arrange["id"], product.id)
        self.assertEqual(arrange["description"], product.description)
        self.assertEqual(arrange["internal_code"], product.internal_code)
        self.assertEqual(arrange["is_active"], product.is_active)
        self.assertEqual(arrange["company"], product.company)
        self.assertEqual(
            str(product), f"{arrange['description']} ({arrange['company'].name})"
        )
