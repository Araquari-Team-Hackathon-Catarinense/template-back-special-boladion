import pytest
from attr.validators import instance_of
from model_bakery import baker
from pycpfcnpj import gen

from core.order.infra.order_django_app.models import MeasurementUnit
from core.order.infra.order_django_app.serializers import (
    MeasurementUnitListSerializer,
)


@pytest.mark.django_db
class TestMeasurementUnitDetailSerializer:
    def test_retrieve_serializer_with_a_specific_measurement_unit(self) -> None:
        measurement_unit = baker.make(MeasurementUnit)
        serializer = MeasurementUnitListSerializer(measurement_unit)
        assert serializer.data == {
            "id": str(measurement_unit.id),
            "description": measurement_unit.description,
        }

    def test_retrieve_serializer_with_no_measurement_unit(self) -> None:
        measurement_unit = {}
        serializer = MeasurementUnitListSerializer(measurement_unit)
        assert serializer.data == {}
