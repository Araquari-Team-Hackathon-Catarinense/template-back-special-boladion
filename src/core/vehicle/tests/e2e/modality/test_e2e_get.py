import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.vehicle.infra.vehicle_django_app.models import Modality

url = "/api/modalities/"


@pytest.mark.django_db
class TestModalityListAPI:
    def test_list_modality(self) -> None:
        created_modalities = baker.make(Modality, _quantity=3)

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
                    "id": str(modality.id),
                    "description": modality.description,
                    "axle": modality.axle,
                }
                for modality in created_modalities
            ],
        }

        assert response.status_code == 200
        assert len(response.json()["results"]) == 3
        assert json.loads(response.content) == expected_data
