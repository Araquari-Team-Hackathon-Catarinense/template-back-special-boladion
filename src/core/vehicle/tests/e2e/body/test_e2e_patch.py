import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.vehicle.infra.vehicle_django_app.models import Body
from django_project.settings import API_VERSION


@pytest.mark.django_db
class TestPatchBodyAPI:
    def test_patch_a_valid_body(self) -> None:

        body: Body = baker.make(Body)

        url = f"/api/{API_VERSION}/vehicle/bodies/{str(body.id)}/"

        new_data = {
            "description": "New body",
        }

        response = APIClient().patch(url, new_data, format="json")

        expected_data = {
            "id": str(body.id),
            "description": new_data["description"],
        }
        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_body(self) -> None:
        url = f"/api/{API_VERSION}/vehicle/bodies/12345678-1234-1234-1234-123456789012/"
        new_data = {
            "description": "New Body",
        }
        response = APIClient().patch(url, new_data, format="json")
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Body matches the given query."
        }
