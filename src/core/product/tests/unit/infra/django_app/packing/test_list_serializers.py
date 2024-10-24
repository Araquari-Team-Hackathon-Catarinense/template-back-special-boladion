import pytest
from model_bakery import baker

from core.product.infra.product_django_app.models import Packing
from core.product.infra.product_django_app.serializers import PackingListSerializer


@pytest.mark.django_db
class TestPackingListSerializer:
    def test_list_serializer_with_many_packing(self) -> None:
        packing = baker.make(Packing, _quantity=3)
        serializer = PackingListSerializer(packing, many=True)
        expected_data = [
            {
                "id": str(p.id),
                "company_id": str(p.company.id),
                "description": p.description,
            }
            for p in packing
        ]
        assert serializer.data == expected_data
