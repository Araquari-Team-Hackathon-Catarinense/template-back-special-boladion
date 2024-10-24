import uuid

import pytest
from model_bakery import baker

from core.company.infra.company_django_app.models import Company
from core.product.infra.product_django_app.models import Product
from core.product.infra.product_django_app.serializers import (
    ProductCreateSerializer,
    ProductListSerializer,
)


@pytest.mark.django_db
class TestProductCreateSerializer:
    def test_create_serializer_with_valid_data(self) -> None:
        company = baker.make(Company)

        data = {
            "company": company.id,
            "description": "Produto 1",
            "internal_code": "123",
            "is_active": True,
        }

        serializer = ProductListSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_serializer_with_invalid_data(self) -> None:
        data = {
            "company": uuid.uuid4(),
            "description": "Produto 1",
            "internal_code": "123",
        }
        serializer = ProductCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert "objeto não existe." in serializer.errors["company"][0]

    def test_create_serializer_with_same_internal_code(self) -> None:
        company = baker.make(Company)
        product = baker.make(Product, company=company)

        data = {
            "company": company.id,
            "description": "Produto 1",
            "internal_code": product.internal_code,
            "is_active": True,
        }

        serializer = ProductCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert (
            "Já existe um produto com esse códico"
            in serializer.errors["non_field_errors"][0]
        )

    def test_create_serializer_with_more_products(self) -> None:
        company = baker.make(Company)

        products = [
            {
                "company": company.id,
                "description": "Produto 1",
                "internal_code": "123",
                "is_active": True,
            },
            {
                "company": company.id,
                "description": "Produto 2",
                "internal_code": "321",
                "is_active": True,
            },
        ]

        serializer = ProductCreateSerializer(data=products[0])
        assert serializer.is_valid() is True

        product1 = serializer.save()
        assert product1.id is not None

        serializer = ProductCreateSerializer(data=products[1])
        assert serializer.is_valid() is True

        product2 = serializer.save()
        assert product2.id is not None

        assert product1.id != product2.id
