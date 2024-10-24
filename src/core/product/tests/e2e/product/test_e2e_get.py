import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.product.infra.product_django_app.models import Product


@pytest.mark.django_db
class TestListAPI:
    def test_list_products(self) -> None:
        created_products = baker.make(Product, _quantity=3)

        url = "/api/products/"
        response = APIClient().get(url)

        expected_data = {
            "total": 3,
            "num_pages": 1,
            "page_number": 1,
            "page_size": 20,
            "links": {
                "next": None,
                "previous": None,
            },
            "results": [
                {
                    "id": str(product.id),
                    "description": product.description,
                    "internal_code": product.internal_code,
                    "is_active": product.is_active,
                }
                for product in created_products
            ],
        }

        assert response.status_code == 200
        assert len(response.json()["results"]) == 3
        assert json.loads(response.content) == expected_data
