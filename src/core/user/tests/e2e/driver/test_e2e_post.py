import pytest
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient

from core.user.infra.user_django_app.models import Driver, User


@pytest.mark.django_db
class TestCreatePurchaseSaleOrderAPITest:
    def test_create_valid_driver(self):
        user: User = baker.make(User)

        driver_data: dict = {
            "license_number": "12345632",
            "license_category": "A",
            "valid_until_license": "2024-12-12",
            "phone": "123456789",
            "user": str(user.id),
        }

        response = APIClient().post(
            "/api/drivers/",
            driver_data,
            format="json",
        )
        print(response.json())
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == driver_data

    def test_create_invalid_driver_because_your_valid_lincense_(self):
        user: User = baker.make(User)

        driver_data: dict = {
            "license_number": "12345632",
            "license_category": "A",
            "valid_until_license": "2023-12-12",
            "phone": "123456789",
            "user": str(user.id),
        }

        response = APIClient().post(
            "/api/drivers/",
            driver_data,
            format="json",
        )
        print(response.json())
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {
            "non_field_errors": [
                "A Data de validade da CNH não pode ser menor que a data atual."
            ]
        }
