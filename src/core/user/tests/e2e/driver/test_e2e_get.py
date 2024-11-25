import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.user.infra.user_django_app.models import Driver, User
from core.user.infra.user_django_app.serializers import ParcialUserSerializer
from django_project.settings import API_VERSION


@pytest.mark.django_db
class TestDriverListAPI:
    def test_list_drivers(self) -> None:
        user = baker.make(User)

        driver = baker.make(
            Driver, user=user, license_category="A", valid_until_license="2022-12-12"
        )

        url = f"/api/{API_VERSION}/user/drivers/"

        client = APIClient()
        response = client.get(url)

        assert response.status_code == 200
        assert response.json()["results"] == [
            {
                "id": str(driver.id),
                "user": ParcialUserSerializer(driver.user).data,
                "license_number": driver.license_number,
                "license_category": driver.license_category,
                "valid_until_license": "2022-12-12",
                "phone": driver.phone,
            }
        ]
