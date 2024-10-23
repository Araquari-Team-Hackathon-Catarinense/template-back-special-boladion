import pytest
from model_bakery import baker

from core.company.infra.company_django_app.models import Company
from core.product.infra.product_django_app.serializers import (
    MeasurementUnitCreateSerializer,
)


@pytest.mark.django_db
class TestMeasurementUnitCreateSerializer:
    def test_create_serializer_with_valid_data(self) -> None:
        company = baker.make(Company)
        data = {
            "description": "Unit",
            "company": company.id,
        }
        serializer = MeasurementUnitCreateSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_serializer_with_invalid_data(self) -> None:
        data = {
            "description": True,
            "company": "1",
        }
        serializer = MeasurementUnitCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert "O valor “1” não é um UUID válido" in serializer.errors["company"]

    def test_if_a_new_uuid_is_generated_with_more_measurement_units(self) -> None:
        companies = baker.make(Company, _quantity=2)
        measurement_units = [
            {
                "description": "Unit 1",
                "company": companies[0].id,
            },
            {
                "description": "Unit 2",
                "company": companies[1].id,
            },
        ]

        serializer = MeasurementUnitCreateSerializer(data=measurement_units[0])
        assert serializer.is_valid() is True
        unit1 = serializer.save()
        assert unit1.id is not None

        serializer = MeasurementUnitCreateSerializer(data=measurement_units[1])
        assert serializer.is_valid() is True
        unit2 = serializer.save()
        assert unit2.id is not None
