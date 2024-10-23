import pytest
from pycpfcnpj import gen

from core.company.infra.company_django_app.serializers import PackingCreateSerializer


@pytest.mark.django_db
class TestPackingCreateSerializer:
    def test_create_serializer_with_valid_data(self) -> None:
        data = {
            "company": "4b3d3b3b-3b3b-3b3b-3b3b-3b3b3b3b3b3b",
            "description": "Packing",
        }
        serializer = PackingCreateSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_serializer_with_invalid_data(self) -> None:
        data = {"company": "4b3d3b3b-3b3b-3b3b-3b3b-3b3b3b3b3b3b", "description": None}
        serializer = PackingCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert "Este campo não pode ser nulo." in serializer.errors["description"]
