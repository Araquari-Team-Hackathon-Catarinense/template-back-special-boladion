import pytest
from model_bakery import baker

from core.product.infra.product_django_app.models import Product
from core.product.infra.product_django_app.serializers import ProductListSerializer


@pytest.mark.django_db
class TestProductListSerializer:
    def test_list_serializer_with_many_products(self) -> None:
        products = baker.make(Product, _quantity=3)
        serializer = ProductListSerializer(products, many=True)
        assert len(serializer.data) == 3
        assert serializer.data == [
            {
                "id": str(product.id),
                "description": product.description,
                "internal_code": product.internal_code,
                "is_active": product.is_active,
            }
            for product in products
        ]

    def test_list_serializer_with_no_products(self) -> None:
        products = []
        serializer = ProductListSerializer(products, many=True)
        assert serializer.data == []

    def test_list_serializer_with_one_product(self) -> None:
        product = baker.make(Product)
        serializer = ProductListSerializer(product, many=False)
        assert serializer.data == {
            "id": str(product.id),
            "description": product.description,
            "internal_code": product.internal_code,
            "is_active": product.is_active,
        }
