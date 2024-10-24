# pylint: disable=no-member,protected-access
import unittest

import pytest
from django.db import models

from core.company.infra.company_django_app.models import Company
from core.uploader.infra.uploader_django_app.models import Document


@pytest.mark.django_db()
class TestCategoryModelInt(unittest.TestCase):

    def test_mapping(self):
        table_name = Company._meta.db_table
        self.assertEqual(table_name, "company")

        fields_name = tuple(field.name for field in Company._meta.fields)
        fields_name += tuple(field.name for field in Company._meta.many_to_many)
        self.assertEqual(
            fields_name,
            (
                "deleted_at",
                "deleted_by_cascade",
                "created_at",
                "updated_at",
                "id",
                "name",
                "trade_name",
                "person_type",
                "document_number",
                "is_active",
                "system_admin",
                "address",
                "contacts",
                "avatar",
                "documents",
            ),
        )

        id_field: models.UUIDField = Company.id.field
        self.assertIsInstance(id_field, models.UUIDField)
        self.assertTrue(id_field.primary_key)
        self.assertFalse(id_field.editable)

        name_field: models.CharField = Company.name.field
        self.assertIsInstance(name_field, models.CharField)
        self.assertFalse(name_field.null)
        self.assertFalse(name_field.blank)
        self.assertEqual(name_field.max_length, 255)

        trade_name_field: models.TextField = Company.trade_name.field
        self.assertIsInstance(trade_name_field, models.CharField)
        self.assertTrue(trade_name_field.null)
        self.assertTrue(trade_name_field.blank)
        self.assertEqual(name_field.max_length, 255)

        is_active_field: models.BooleanField = Company.is_active.field
        self.assertIsInstance(is_active_field, models.BooleanField)
        self.assertTrue(is_active_field.default)

        person_type_field: models.CharField = Company.person_type.field
        self.assertIsInstance(person_type_field, models.CharField)
        self.assertEqual(person_type_field.max_length, 2)

        document_number_field: models.CharField = Company.document_number.field
        self.assertIsInstance(document_number_field, models.CharField)
        self.assertEqual(document_number_field.max_length, 14)
        self.assertTrue(document_number_field.unique)

        address_field: models.JSONField = Company.address.field
        self.assertIsInstance(address_field, models.JSONField)
        self.assertTrue(address_field.null)
        self.assertTrue(address_field.blank)

        contacts_field: models.JSONField = Company.contacts.field
        self.assertIsInstance(contacts_field, models.JSONField)
        self.assertTrue(contacts_field.null)
        self.assertTrue(contacts_field.blank)

        system_admin_field: models.BooleanField = Company.system_admin.field
        self.assertIsInstance(system_admin_field, models.BooleanField)
        self.assertFalse(system_admin_field.default)

        documents_field = Company.documents.field
        self.assertIsInstance(documents_field, models.ManyToManyField)
        self.assertEqual(documents_field.related_model, Document)
        self.assertTrue(documents_field.blank)

        avatar_field: models.ForeignKey = Company.avatar.field
        self.assertIsInstance(avatar_field, models.ForeignKey)
        self.assertEqual(avatar_field.related_model, Document)

    def test_create(self):
        arrange = {
            "id": "af46842e-027d-4c91-b259-3a3642144ba4",
            "name": "Company",
            "trade_name": "Company Trade",
            "person_type": "PJ",
            "document_number": "00000000000000",
            "is_active": True,
            "address": {"city": "City", "state": "State"},
            "contacts": [{"phone": "00000000000"}],
            "avatar": None,
        }
        company = Company.objects.create(**arrange)
        documents = Document.objects.create(file="th.jpg", description="Description")
        company.documents.add(documents)

        self.assertEqual(company.id, arrange["id"])
        self.assertEqual(company.name, arrange["name"])
        self.assertEqual(company.trade_name, arrange["trade_name"])
        self.assertEqual(company.person_type, arrange["person_type"])
        self.assertEqual(company.document_number, arrange["document_number"])
        self.assertEqual(company.is_active, arrange["is_active"])
        self.assertEqual(company.address, arrange["address"])
        self.assertEqual(company.contacts, arrange["contacts"])
        self.assertEqual(company.system_admin, False)
        self.assertEqual(company.documents.first(), documents)
        self.assertEqual(
            str(company), f"{arrange['name']} ({arrange['document_number']})"
        )
        self.assertIsNotNone(company.avatar)
