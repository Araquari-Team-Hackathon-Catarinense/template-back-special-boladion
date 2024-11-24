import unittest

import pytest
from django.db import models

from core.order.infra.order_django_app.models import Trip


@pytest.mark.django_db()
class TestTripUnitModelsInt(unittest.TestCase):
    def test_mapping(self):
        table_name = Trip._meta.db_table
        assert table_name == "order_django_app_trip"

        fields_name = tuple(field.name for field in Trip._meta.fields)
        assert fields_name == (
            "deleted_at",
            "deleted_by_cascade",
            "created_at",
            "updated_at",
            "id",
            "transport_contract",
            "quantity",
            "date",
            "order_number",
            "vehicle",
            "driver",
        )

        id_field = Trip.id.field
        assert isinstance(id_field, models.UUIDField)
        assert id_field.primary_key is True

        transport_contract_field = Trip.transport_contract.field
        assert isinstance(transport_contract_field, models.ForeignKey)
        assert transport_contract_field.null is True

        quantity_field = Trip.quantity.field
        assert isinstance(quantity_field, models.FloatField)
        assert quantity_field.blank is True
        assert quantity_field.null is True

        date_field = Trip.date.field
        assert isinstance(date_field, models.DateField)
        assert date_field.blank is True
        assert date_field.null is True

        order_number_field = Trip.order_number.field
        assert isinstance(order_number_field, models.CharField)
        assert order_number_field.max_length == 45
        assert order_number_field.blank is True
        assert order_number_field.null is True

        driver_field = Trip.driver.field
        assert isinstance(driver_field, models.ForeignKey)

        vehicle_field = Trip.vehicle.field
        assert isinstance(vehicle_field, models.ForeignKey)
