# pylint: disable=no-member,protected-access
import unittest

import pytest
from django.db import models

from core.vehicle.infra.vehicle_django_app.models import Body


@pytest.mark.django_db()
class TestOperationModelInt(unittest.TestCase):

    def test_mapping(self):
        table_name = Body._meta.db_table
        self.assertEqual(table_name, "body")

        fields_name = tuple(field.name for field in Body._meta.fields)
        self.assertEqual(
            fields_name,
            ("id", "description"),
        )

        id_field: models.UUIDField = Body.id.field
        self.assertIsInstance(id_field, models.UUIDField)
        self.assertTrue(id_field.primary_key)
        self.assertTrue(id_field.editable)

        description_field: models.CharField = Body.description.field
        self.assertIsInstance(description_field, models.CharField)
        self.assertEqual(description_field.max_length, 45)

    def test_create(self):
        arrange = {
            "id": "af46842e-027d-4c91-b259-3a3642144ba4",
            "description": "My Body",
        }

        body = Body.objects.create(**arrange)

        self.assertEqual(body.id, arrange["id"])
        self.assertEqual(body.description, arrange["description"])
