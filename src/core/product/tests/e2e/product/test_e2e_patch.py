import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.product.infra.product_django_app.models import Product


@pytest.mark.django_db
class TestPatchAPI:
    def test_patch_a_valid_product(self) -> None:
        product = baker.make(Product)

        url = f"/api/products/{product.id}/"

        new_data = {
            "description": product.description,
        }

        response = APIClient().patch(url, new_data, format="json")

        expected_data = {
            "id": str(product.id),
            "description": new_data["description"],
            "internal_code": product.internal_code,
            "is_active": product.is_active,
            "company": str(product.company.id),
        }

        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_product(self) -> None:
        url = "/api/products/12345678-1234-1234-1234-123456789012/"
        new_data = {
            "is_active": False,
        }
        response = APIClient().patch(url, new_data, format="json")
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Product matches the given query."
        }
