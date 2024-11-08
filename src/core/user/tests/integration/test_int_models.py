import unittest

import pytest
from django.db import models

from core.user.infra.user_django_app.models import Driver, User


@pytest.mark.django_db()
class TestDriverModelInt(unittest.TestCase):

    def test_mapping(self):
        table_name = Driver._meta.db_table
        self.assertEqual(table_name, "user_django_app_driver")

        fields_name = tuple(field.name for field in Driver._meta.fields)
        self.assertEqual(
            fields_name,
            (
                "deleted_at",
                "deleted_by_cascade",
                "created_at",
                "updated_at",
                "id",
                "user",
                "license_number",
                "license_category",
                "valid_until_license",
                "phone",
            ),
        )

        id_field: models.UUIDField = Driver.id.field
        self.assertIsInstance(id_field, models.UUIDField)
        self.assertTrue(id_field.primary_key)
        self.assertFalse(id_field.editable)

        license_number_field: models.CharField = Driver.license_number.field
        self.assertIsInstance(license_number_field, models.CharField)
        self.assertTrue(license_number_field.null)

        license_category_field: models.CharField = Driver.license_category.field
        self.assertIsInstance(license_category_field, models.CharField)
        self.assertTrue(license_category_field.null)
        self.assertTrue(license_category_field.blank)

        valid_until_license_field: models.DateField = Driver.valid_until_license.field
        self.assertIsInstance(valid_until_license_field, models.DateField)
        self.assertTrue(valid_until_license_field.null)

        phone_field: models.CharField = Driver.phone.field
        self.assertIsInstance(phone_field, models.CharField)
        self.assertTrue(phone_field.null)
        self.assertTrue(phone_field.blank)

        user_field: models.ForeignKey = Driver.user.field
        self.assertIsInstance(user_field, models.ForeignKey)
