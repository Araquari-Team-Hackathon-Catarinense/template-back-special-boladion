# pylint: disable=no-member,protected-access
import unittest

import pytest
from django.db import models
from model_bakery import baker

from core.company.infra.company_django_app.models import Company, Contract
from core.parking.infra.parking_django_app.models import Parking, ParkingSector


@pytest.mark.django_db()
class TestParkingSectorModelInt(unittest.TestCase):

    def test_mapping(self):
        table_name = ParkingSector._meta.db_table
        self.assertEqual(table_name, "parking_sector")

        fields_name = tuple(field.name for field in ParkingSector._meta.fields)
        self.assertEqual(
            fields_name,
            (
                "deleted_at",
                "deleted_by_cascade",
                "created_at",
                "updated_at",
                "id",
                "description",
                "qty_slots",
                "sector_type",
                "parking",
                "contract",
            ),
        )

        id_field: models.UUIDField = ParkingSector.id.field
        self.assertIsInstance(id_field, models.UUIDField)
        self.assertTrue(id_field.primary_key)

        description_field: models.CharField = ParkingSector.description.field
        self.assertIsInstance(description_field, models.CharField)
        self.assertFalse(description_field.null)
        self.assertFalse(description_field.blank)
        self.assertEqual(description_field.max_length, 45)

        qty_slots_field: models.IntegerField = ParkingSector.qty_slots.field
        self.assertIsInstance(qty_slots_field, models.IntegerField)
        self.assertEqual(qty_slots_field.default, 0)

        sector_type_field: models.CharField = ParkingSector.sector_type.field
        self.assertIsInstance(sector_type_field, models.CharField)
        self.assertFalse(sector_type_field.null)
        self.assertFalse(sector_type_field.blank)
        self.assertEqual(sector_type_field.max_length, 8)

        parking_field: models.ForeignKey = ParkingSector.parking.field
        self.assertIsInstance(parking_field, models.ForeignKey)
        self.assertEqual(parking_field.related_model, Parking)

        contract_field: models.ForeignKey = ParkingSector.contract.field
        self.assertIsInstance(contract_field, models.ForeignKey)
        self.assertEqual(contract_field.related_model, Contract)

        created_at_field: models.DateTimeField = ParkingSector.created_at.field
        self.assertIsInstance(created_at_field, models.DateTimeField)

        updated_at_field: models.DateTimeField = ParkingSector.updated_at.field
        self.assertIsInstance(updated_at_field, models.DateTimeField)

    def test_create(self):
        company = Company.objects.create(
            name="Company",
            person_type="PJ",
            document_number="12345678901234",
        )
        parking = Parking.objects.create(
            description="Parking",
            company=company,
        )
        contract = baker.make(Contract)
        arrange = {
            "id": "af46842e-027d-4c91-b259-3a3642144ba4",
            "description": "Parking Sector",
            "qty_slots": 100,
            "sector_type": "CONTRACT",
            "parking": parking,
            "contract": contract,
        }

        parking_sector = ParkingSector.objects.create(**arrange)

        self.assertEqual(parking_sector.id, arrange["id"])
        self.assertEqual(parking_sector.description, arrange["description"])
        self.assertEqual(parking_sector.qty_slots, arrange["qty_slots"])
        self.assertEqual(parking_sector.sector_type, arrange["sector_type"])
        self.assertEqual(parking_sector.parking, arrange["parking"])
        self.assertEqual(parking_sector.contract, arrange["contract"])
