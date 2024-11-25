import uuid

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from django_project.settings import API_VERSION

url = f"/api/{API_VERSION}/vehicle/bodies/"


@pytest.mark.django_db
class TestBodyListAPI:
    def test_create_a_valid_body(self) -> None:
        body = {
            "description": "body 1",
        }

        response = APIClient().post(
            url,
            {
                "description": body["description"],
            },
        )

        assert response.status_code == 201
        assert response.json() == {
            "id": response.json()["id"],
            "description": body["description"],
        }

    def test_if_create_a_body_not_passing_the_description(
        self,
    ) -> None:
        body = {}

        response = APIClient().post(
            url,
            body,
        )

        assert response.status_code == 400
        assert "Este campo é obrigatório." in response.json()["description"][0]
