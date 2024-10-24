# pylint: disable=no-member,protected-access
import unittest

from model_bakery import baker
import pytest
from django.db import models

from core.company.infra.company_django_app.models import Company, Contract


@pytest.mark.django_db()
class TestContractModelInt(unittest.TestCase):

    def test_mapping(self):
        table_name = Contract._meta.db_table
        self.assertEqual(table_name, "contract")

        fields_name = tuple(field.name for field in Contract._meta.fields)
        self.assertEqual(
            fields_name,
            (
                "deleted_at",
                "deleted_by_cascade",
                "created_at",
                "updated_at",
                "id",
                "source_company",
                "target_company",
                "contract_type"            ),
        )

        id_field: models.UUIDField = Contract.id.field
        self.assertIsInstance(id_field, models.UUIDField)
        self.assertTrue(id_field.primary_key)
        self.assertFalse(id_field.editable)

        contract_type_field: models.CharField = Contract.contract_type.field
        self.assertIsInstance(contract_type_field, models.CharField)
        self.assertEqual(contract_type_field.max_length, 255)

        source_company_field: models.ForeignKey = Contract.source_company.field
        self.assertIsInstance(source_company_field, models.ForeignKey)
        self.assertFalse(source_company_field.blank)
        self.assertFalse(source_company_field.null)

        target_company_field: models.ForeignKey = Contract.target_company.field
        self.assertIsInstance(target_company_field, models.ForeignKey)
        self.assertFalse(target_company_field.blank)
        self.assertFalse(target_company_field.null)


    def test_create(self):
        source_company = baker.make(Company)
        target_company = baker.make(Company)

        arrange = {
            "id": "af46842e-027d-4c91-b259-3a3642144ba4",
            "source_company": source_company,
            "target_company": target_company,
            "contract_type": "CLIENTE"
        }
        contract = Contract.objects.create(**arrange)
        self.assertEqual(contract.id, arrange["id"])
        self.assertEqual(contract.source_company.id, source_company.id)
        self.assertEqual(contract.target_company.id, target_company.id)
        self.assertEqual(
            str(contract), f"{source_company.name} - {target_company.name} ({arrange['contract_type']})"
        )
