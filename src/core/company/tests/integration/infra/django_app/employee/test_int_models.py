# pylint: disable=no-member,protected-access
import unittest

import pytest
from django.db import models
from model_bakery import baker

from core.company.infra.company_django_app.models import Company, Employee
from core.user.infra.user_django_app.models import User


@pytest.mark.django_db()
class TestCategoryModelInt(unittest.TestCase):

    def test_mapping(self):
        table_name = Employee._meta.db_table
        self.assertEqual(table_name, "employee")

        fields_name = tuple(field.name for field in Employee._meta.fields)
        self.assertEqual(
            fields_name,
            ("deleted_at",
             "deleted_by_cascade",
             "created_at",
             "updated_at",
             "id",
             "company",
             "user",
             "is_active",
            ),
        )

        id_field: models.UUIDField = Employee.id.field
        self.assertIsInstance(id_field, models.UUIDField)
        self.assertTrue(id_field.primary_key)
        self.assertFalse(id_field.editable)

        company_field: models.ForeignKey = Employee.company.field
        self.assertIsInstance(company_field, models.ForeignKey)
        self.assertFalse(company_field.blank)
        self.assertFalse(company_field.null)

        user_field: models.ForeignKey = Employee.user.field
        self.assertIsInstance(user_field, models.ForeignKey)
        self.assertFalse(user_field.blank)
        self.assertFalse(user_field.null)

        is_active_field: models.BooleanField = Employee.is_active.field
        self.assertIsInstance(is_active_field, models.BooleanField)
        self.assertTrue(is_active_field.blank)
        self.assertTrue(is_active_field.null)
        self.assertTrue(is_active_field.editable)
        self.assertTrue(is_active_field.default)

    def test_create(self):
        company = baker.make(Company)
        user = baker.make(User)
        arrange = {
            "id": "af46842e-027d-4c91-b259-3a3642144ba4",
            "company": company,
            "user": user,
            "is_active": True,
        }

        employee = Employee.objects.create(**arrange)

        self.assertEqual(arrange["id"], employee.id)
        self.assertEqual(arrange["company"], employee.company)
        self.assertEqual(arrange["user"], employee.user)
        self.assertEqual(arrange["is_active"], employee.is_active)
        self.assertEqual(str(employee), f"{arrange['user']} ({arrange['company']})")
