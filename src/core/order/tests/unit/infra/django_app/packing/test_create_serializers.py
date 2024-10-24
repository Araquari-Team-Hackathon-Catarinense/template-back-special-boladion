from model_bakery import baker
import pytest

from core.company.infra.company_django_app.models import Company
from core.order.infra.order_django_app.serializers import PackingCreateSerializer


@pytest.mark.django_db
class TestPackingCreateSerializer:
    def test_create_serializer_with_valid_data(self) -> None:
        company = baker.make(Company)
        data = {
            "company": str(company.id),
            "description": "Packing",
        }
        serializer = PackingCreateSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_serializer_with_invalid_data(self) -> None:
        company = baker.make(Company)
        data = {"company": str(company.id), "description": None}
        serializer = PackingCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert "Este campo não pode ser nulo." in serializer.errors["description"]
