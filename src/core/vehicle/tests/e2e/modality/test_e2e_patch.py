import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.vehicle.infra.vehicle_django_app.models import Modality
from django_project.settings import API_VERSION


@pytest.mark.django_db
class TestPatchModalityAPI:
    def test_patch_a_valid_modality(self) -> None:

        modality: Modality = baker.make(Modality)

        url = f"/api/{API_VERSION}/vehicle/modalities/{str(modality.id)}/"

        new_data = {
            "description": "New modality",
        }

        response = APIClient().patch(url, new_data, format="json")

        expected_data = {
            "id": str(modality.id),
            "description": new_data["description"],
            "axle": modality.axle,
        }
        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_modality(self) -> None:
        url = f"/api/{API_VERSION}/vehicle/modalities/12345678-1234-1234-1234-123456789012/"
        new_data = {
            "description": "New Modality",
        }
        response = APIClient().patch(url, new_data, format="json")
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Modality matches the given query."
        }
