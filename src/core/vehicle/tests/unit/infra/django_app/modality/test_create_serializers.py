import pytest

from core.vehicle.infra.vehicle_django_app.views import ModalityCreateSerializer


@pytest.mark.django_db
class TestModalityCreateSerializer:
    def test_create_serializer_with_valid_modality(self) -> None:
        data = {
            "description": "My Modality",
            "axle": "My Axle",
        }

        serializer = ModalityCreateSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_serializer_with_invalid_data(self) -> None:
        data = {}
        serializer = ModalityCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert f"Este campo é obrigatório." in serializer.errors["description"]
        assert f"Este campo é obrigatório." in serializer.errors["axle"]
