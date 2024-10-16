# pylint: disable=no-member,protected-access
import unittest

from core.company.infra.company_django_app.models import Company
import pytest
from django.db import models

from core.parking.infra.parking_django_app.models import Parking


@pytest.mark.django_db()
class TestParkingModelInt(unittest.TestCase):

    def test_mapping(self):
        table_name = Parking._meta.db_table
        self.assertEqual(table_name, "parking")

        fields_name = tuple(field.name for field in Parking._meta.fields)
        self.assertEqual(
            fields_name,
            (
                "id",
                "description",
                "slots",
                "entity",
            ),
        )

        id_field: models.UUIDField = Parking.id.field
        self.assertIsInstance(id_field, models.UUIDField)
        self.assertTrue(id_field.primary_key)
        self.assertTrue(id_field.editable)

        description_field: models.CharField = Parking.description.field
        self.assertIsInstance(description_field, models.CharField)
        self.assertFalse(description_field.null)
        self.assertFalse(description_field.blank)
        self.assertEqual(description_field.max_length, 45)

        slots_field: models.IntegerField = Parking.slots.field
        self.assertIsInstance(slots_field, models.IntegerField)
        self.assertEqual(slots_field.default, 0)

        entity_field: models.ForeignKey = Parking.entity.field
        self.assertIsInstance(entity_field, models.ForeignKey)
        self.assertEqual(entity_field.related_model, Company)

    def test_create(self):
        company = Company.objects.create(
            name="Company",
            person_type="PJ",
            document_number="12345678901234",
        )
        arrange = {
            "id": "af46842e-027d-4c91-b259-3a3642144ba4",
            "description": "Parking",
            "slots": 100,
            "entity": company,
        }

        parking = Parking.objects.create(**arrange)

        self.assertEqual(parking.id, arrange["id"])
        self.assertEqual(parking.description, arrange["description"])
        self.assertEqual(parking.slots, arrange["slots"])
        self.assertEqual(parking.entity, arrange["entity"])
