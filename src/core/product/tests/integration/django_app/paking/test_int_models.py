# pylint: disable=no-member,protected-access
import unittest
import uuid

import pytest
from django.db import models
from model_bakery import baker

from core.company.infra.company_django_app.models import Company
from core.product.infra.product_django_app.models import Packing


@pytest.mark.django_db()
class TestPakingUnitModelInt(unittest.TestCase):

    def test_mapping(self):
        table_name = Packing._meta.db_table
        self.assertEqual(table_name, "product_django_app_packing")

        fields_name = tuple(field.name for field in Packing._meta.fields)
        self.assertEqual(
            fields_name,
            (
                "id",
                "company",
                "description",
            ),
        )

        id_field: models.UUIDField = Packing.id.field
        self.assertIsInstance(id_field, models.UUIDField)
        self.assertTrue(id_field.primary_key)
        self.assertTrue(id_field.editable)

        description_field: models.CharField = Packing.description.field
        self.assertIsInstance(description_field, models.CharField)
        self.assertFalse(description_field.null)
        self.assertFalse(description_field.blank)
        self.assertEqual(description_field.max_length, 255)

        company_field: models.ForeignKey = Packing.company.field
        self.assertIsInstance(company_field, models.ForeignKey)
        self.assertFalse(company_field.blank)
        self.assertFalse(company_field.null)

    def test_create(self):
        company = baker.make(Company)
        id = uuid.uuid4()
        arrange = {
            "id": id,
            "description": "description",
            "company": company,
        }
        packing_unit = Packing.objects.create(
            id=arrange["id"],
            description=arrange["description"],
            company=arrange["company"],
        )

        self.assertEqual(packing_unit.id, arrange["id"])
