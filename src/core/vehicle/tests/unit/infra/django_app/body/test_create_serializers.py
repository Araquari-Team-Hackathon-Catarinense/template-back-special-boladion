import pytest

from core.vehicle.infra.vehicle_django_app.models import Body
from core.vehicle.infra.vehicle_django_app.views import BodyCreateSerializer


@pytest.mark.django_db
class TestBodyCreateSerializer:
    def test_create_serializer_with_valid_operation(self) -> None:
        data = {
            "description": "My Body",
        }

        serializer = BodyCreateSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_serializer_with_invalid_data(self) -> None:
        data = {}
        serializer = BodyCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert f"Este campo é obrigatório." in serializer.errors["description"]
