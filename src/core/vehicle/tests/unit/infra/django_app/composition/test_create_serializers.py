import pytest

from core.vehicle.infra.vehicle_django_app.views import CompositionCreateSerializer


@pytest.mark.django_db
class TestCompositionCreateSerializer:
    def test_create_serializer_with_valid_data(self) -> None:
        data = {
            "axle": 2,
            "gross_weight": 50,
            "is_active": True,
        }

        serializer = CompositionCreateSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_serializer_with_invalid_data(self) -> None:
        data = {
            "axle": "3",
            "is_active": 0,
        }

        serializer = CompositionCreateSerializer(data=data)
        assert serializer.is_valid() is False

        assert f"Este campo é obrigatório." in serializer.errors["gross_weight"]
        assert f"Oi" in serializer.errors["is_active"]
