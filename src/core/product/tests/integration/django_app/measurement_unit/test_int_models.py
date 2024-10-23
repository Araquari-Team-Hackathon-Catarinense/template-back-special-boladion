# pylint: disable=no-member,protected-access
import unittest

import pytest
from django.db import models
from model_bakery import baker

from core.company.infra.company_django_app.models import Company
from core.product.infra.product_django_app.models import MeasurementUnit


@pytest.mark.django_db()
class TestMeasurementUnitModelInt(unittest.TestCase):

    def test_mapping(self):
        table_name = MeasurementUnit._meta.db_table
        self.assertEqual(table_name, "measurement_unit")

        fields_name = tuple(field.name for field in MeasurementUnit._meta.fields)
        self.assertEqual(
            fields_name,
            (
                "id",
                "description",
                "company",
            ),
        )

        id_field: models.UUIDField = MeasurementUnit.id.field
        self.assertIsInstance(id_field, models.UUIDField)
        self.assertTrue(id_field.primary_key)
        self.assertTrue(id_field.editable)

        description_field: models.CharField = MeasurementUnit.description.field
        self.assertIsInstance(description_field, models.CharField)
        self.assertFalse(description_field.null)
        self.assertFalse(description_field.blank)
        self.assertEqual(description_field.max_length, 45)

        company_field: models.ForeignKey = MeasurementUnit.company.field
        self.assertIsInstance(company_field, models.ForeignKey)
        self.assertFalse(company_field.blank)
        self.assertFalse(company_field.null)

    def test_create(self):
        company = baker.make(Company)
        arrange = {
            "id": "f4b3b3b3-3b3b-4b4b-b3b3-b3b3b3b3b3b3",
            "description": "description",
            "company": company,
        }
        measurement_unit = MeasurementUnit.objects.create(
            id=arrange["id"],
            description=arrange["description"],
            company=arrange["company"],
        )
        self.assertEqual(measurement_unit.id, arrange["id"])
        self.assertEqual(measurement_unit.description, arrange["description"])
        self.assertEqual(measurement_unit.company, arrange["company"])
        self.assertEqual(str(measurement_unit), f"{arrange['description']}")
