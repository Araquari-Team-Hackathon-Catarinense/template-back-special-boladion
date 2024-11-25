import uuid

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from django_project.settings import API_VERSION

url = f"/api/{API_VERSION}/vehicle/modalities/"


@pytest.mark.django_db
class TestModalityistAPI:
    def test_create_a_valid_modality(self) -> None:
        modality = {
            "description": "modality 1",
            "axle": 3,
        }

        response = APIClient().post(
            url,
            {
                "description": modality["description"],
                "axle": modality["axle"],
            },
        )

        assert response.status_code == 201
        assert response.json() == {
            "id": response.json()["id"],
            "description": modality["description"],
            "axle": modality["axle"],
        }

    def test_if_create_a_modality_not_passing_the_description_and_axle(
        self,
    ) -> None:
        modality = {}

        response = APIClient().post(
            url,
            modality,
        )

        assert response.status_code == 400
        assert "Este campo é obrigatório." in response.json()["description"][0]
        assert "Este campo é obrigatório." in response.json()["axle"][0]
