import pytest
from model_bakery import baker

from core.product.infra.product_django_app.models import MeasurementUnit
from core.product.infra.product_django_app.serializers import (
    MeasurementUnitListSerializer,
)


@pytest.mark.django_db
class TestCompanyListSerializer:
    def test_list_serializer_with_many_measurement_units(self) -> None:
        measurement_units = baker.make(MeasurementUnit, _quantity=3)
        serializer = MeasurementUnitListSerializer(measurement_units, many=True)
        assert serializer.data == [
            {
                "id": str(measurement_unit.id),
                "description": measurement_unit.description,
                "company": str(measurement_unit.company.id),
            }
            for measurement_unit in measurement_units
        ]

    def test_list_serializer_with_no_measurement_units(self) -> None:
        measurement_units = []
        serializer = MeasurementUnitListSerializer(measurement_units, many=True)
        assert serializer.data == []

    def test_list_serializer_with_one_measurement_unit(self) -> None:
        measurement_unit = baker.make(MeasurementUnit)
        serializer = MeasurementUnitListSerializer(measurement_unit, many=False)
        assert serializer.data == {
            "id": str(measurement_unit.id),
            "description": measurement_unit.description,
            "company": str(measurement_unit.company.id),
        }
