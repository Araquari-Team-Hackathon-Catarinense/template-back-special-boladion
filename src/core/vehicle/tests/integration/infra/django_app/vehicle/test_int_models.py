# pylint: disable=no-member,protected-access
import unittest

import pytest
from django.db import models

from core.vehicle.infra.vehicle_django_app.models import Body, Modality, Vehicle


@pytest.mark.django_db()
class TestVehicleModelInt(unittest.TestCase):

    def test_mapping(self):
        table_name = Vehicle._meta.db_table
        self.assertEqual(table_name, "vehicle_django_app_vehicle")

        fields_name = tuple(field.name for field in Vehicle._meta.fields)
        self.assertEqual(
            fields_name,
            (
                "deleted_at",
                "deleted_by_cascade",
                "created_at",
                "updated_at",
                "id",
                "license",
                "chassis",
                "renavam",
                "axle",
                "year",
                "gross_weight",
                "vehicle_type",
                "body",
                "modality",
            ),
        )

        id_field: models.UUIDField = Vehicle.id.field
        self.assertIsInstance(id_field, models.UUIDField)
        self.assertTrue(id_field.primary_key)

        license_field: models.CharField = Vehicle.license.field
        self.assertIsInstance(license_field, models.CharField)
        self.assertEqual(license_field.max_length, 10)
        self.assertTrue(license_field.unique)

        chassis_field: models.CharField = Vehicle.chassis.field
        self.assertIsInstance(chassis_field, models.CharField)
        self.assertEqual(chassis_field.max_length, 45)
        self.assertTrue(chassis_field.blank)
        self.assertTrue(chassis_field.null)
        self.assertTrue(chassis_field.unique)

        renavam_field: models.CharField = Vehicle.renavam.field
        self.assertIsInstance(renavam_field, models.CharField)
        self.assertEqual(renavam_field.max_length, 45)
        self.assertTrue(renavam_field.blank)
        self.assertTrue(renavam_field.null)

        axle_field: models.IntegerField = Vehicle.axle.field
        self.assertIsInstance(axle_field, models.IntegerField)
        self.assertTrue(axle_field.blank)
        self.assertTrue(axle_field.null)

        year_field: models.IntegerField = Vehicle.year.field
        self.assertIsInstance(year_field, models.IntegerField)
        self.assertTrue(year_field.blank)
        self.assertTrue(year_field.null)

        gross_weight_field: models.IntegerField = Vehicle.gross_weight.field
        self.assertIsInstance(gross_weight_field, models.IntegerField)
        self.assertTrue(gross_weight_field.blank)
        self.assertTrue(gross_weight_field.null)

        vehicle_type_field: models.CharField = Vehicle.vehicle_type.field
        self.assertIsInstance(vehicle_type_field, models.CharField)
        self.assertEqual(vehicle_type_field.max_length, 45)
        self.assertEqual(
            vehicle_type_field.choices,
            [(vehicle_type) for vehicle_type in Vehicle.VEHICLE_TYPE_CHOICES],
        )

        body_field: models.ForeignKey = Vehicle.body.field
        self.assertIsInstance(body_field, models.ForeignKey)
        self.assertTrue(body_field.null)
        self.assertTrue(body_field.blank)
        self.assertEqual(body_field._related_name, "body")

        modality_field: models.ForeignKey = Vehicle.modality.field
        self.assertIsInstance(modality_field, models.ForeignKey)

        self.assertTrue(modality_field.null)
        self.assertTrue(modality_field.blank)
        self.assertEqual(modality_field._related_name, "modality")

    def test_create(self):
        # Dados de exemplo para o teste
        arrange = {
            "id": "af46842e-027d-4c91-b259-3a3642144ba4",
            "license": "ABC1234",
            "chassis": "CHASSIS123",
            "renavam": "RENAVAM123",
            "axle": 4,
            "year": 2022,
            "gross_weight": 15000,
            "vehicle_type": "Caminhão",
            "body": Body.objects.create(
                description="Container", id="af46842e-027d-4c91-b259-3a3642144ba4"
            ),
            "modality": Modality.objects.create(
                description="Transporte de carga",
                axle=4,
                id="af46842e-027d-4c91-b259-3a3642144ba4",
            ),
        }

        vehicle = Vehicle.objects.create(**arrange)

        self.assertEqual(vehicle.id, arrange["id"])
        self.assertEqual(vehicle.license, arrange["license"])
        self.assertEqual(vehicle.chassis, arrange["chassis"])
        self.assertEqual(vehicle.renavam, arrange["renavam"])
        self.assertEqual(vehicle.axle, arrange["axle"])
        self.assertEqual(vehicle.year, arrange["year"])
        self.assertEqual(vehicle.gross_weight, arrange["gross_weight"])
        self.assertEqual(vehicle.vehicle_type, arrange["vehicle_type"])
        self.assertEqual(vehicle.body, arrange["body"])
        self.assertEqual(vehicle.modality, arrange["modality"])
