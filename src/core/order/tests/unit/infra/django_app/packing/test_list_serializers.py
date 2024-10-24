import pytest
from model_bakery import baker

from core.order.infra.order_django_app.models import Packing
from core.order.infra.order_django_app.serializers import PackingListSerializer


@pytest.mark.django_db
class TestPackingListSerializer:
    def test_list_serializer_with_many_packing(self) -> None:
        packings = baker.make(Packing, _quantity=3)
        serializer = PackingListSerializer(packings, many=True)
        expected_data = [
            {
                "id": str(packing.id),
                "description": packing.description,
            }
            for packing in packings
        ]
        assert serializer.data == expected_data
