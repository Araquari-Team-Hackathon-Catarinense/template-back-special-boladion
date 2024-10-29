# pylint: disable=no-member,protected-access
import unittest

import pytest
from django.db import models

from core.vehicle.infra.vehicle_django_app.models import Modality


@pytest.mark.django_db()
class TestModalityModelInt(unittest.TestCase):

    def test_mapping(self):
        table_name = Modality._meta.db_table
        self.assertEqual(table_name, "modality")

        fields_name = tuple(field.name for field in Modality._meta.fields)
        self.assertEqual(
            fields_name,
            ("id", "description", "axle"),
        )

        id_field: models.UUIDField = Modality.id.field
        self.assertIsInstance(id_field, models.UUIDField)
        self.assertTrue(id_field.primary_key)
        self.assertTrue(id_field.editable)

        description_field: models.CharField = Modality.description.field
        self.assertIsInstance(description_field, models.CharField)
        self.assertEqual(description_field.max_length, 45)

        axle_field: models.IntegerField = Modality.axle.field
        self.assertIsInstance(axle_field, models.IntegerField)

    def test_create(self):
        arrange = {
            "id": "af46842e-027d-4c91-b259-3a3642144ba4",
            "description": "My Modality",
            "axle": 3,
        }

        modality = Modality.objects.create(**arrange)

        self.assertEqual(modality.id, arrange["id"])
        self.assertEqual(modality.description, arrange["description"])
        self.assertEqual(modality.axle, arrange["axle"])
