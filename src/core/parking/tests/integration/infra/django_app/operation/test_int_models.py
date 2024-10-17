# pylint: disable=no-member,protected-access
import unittest

import pytest
from django.db import models

from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import Operation, Parking


@pytest.mark.django_db()
class TestOperationModelInt(unittest.TestCase):

    def test_mapping(self):
        table_name = Operation._meta.db_table
        self.assertEqual(table_name, "operation")

        fields_name = tuple(field.name for field in Operation._meta.fields)
        self.assertEqual(
            fields_name,
            ("id", "name", "parking"),
        )

        id_field: models.UUIDField = Operation.id.field
        self.assertIsInstance(id_field, models.UUIDField)
        self.assertTrue(id_field.primary_key)
        self.assertTrue(id_field.editable)

        name_field: models.CharField = Operation.name.field
        self.assertIsInstance(name_field, models.CharField)
        self.assertFalse(name_field.null)
        self.assertFalse(name_field.blank)
        self.assertEqual(name_field.max_length, 45)

        parking_field: models.ForeignKey = Operation.parking.field
        self.assertIsInstance(parking_field, models.ForeignKey)
        self.assertEqual(parking_field.related_model, Parking)

    def test_create(self):
        company = Company.objects.create(
            name="Company",
            person_type="PJ",
            document_number="12345678901234",
        )
        parking = Parking.objects.create(
            description="Parking",
            entity=company,
        )
        arrange = {
            "id": "af46842e-027d-4c91-b259-3a3642144ba4",
            "name": "My Operation",
            "parking": parking,
        }

        operation = Operation.objects.create(**arrange)

        self.assertEqual(operation.id, arrange["id"])
        self.assertEqual(operation.name, arrange["name"])
        self.assertEqual(operation.parking, arrange["parking"])
