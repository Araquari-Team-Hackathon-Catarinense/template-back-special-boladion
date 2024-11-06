import uuid

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.vehicle.infra.vehicle_django_app.models import Body, Modality, Vehicle


@pytest.mark.django_db
class TestListAPI:
    def test_create_a_valid_vehicle(self) -> None:
        url: str = "/api/vehicles/"

        body: Body = baker.make(Body)
        modality: Modality = baker.make(Modality)

        response = APIClient().post(
            url,
            {
                "license": "fjdj",
                "chassis": "438743875378",
                "renavam": "745783475",
                "axle": 2,
                "year": 2021,
                "gross_weight": 1000,
                "vehicle_type": "TRACIONADORA",
                "body": body.id,
                "modality": modality.id,
            },
        )
        print(response.json())
        assert response.status_code == 201

    def test_if_throw_error_with_invalid_vehicle(self) -> None:
        url = "/api/vehicles/"

        body: Body = baker.make(Body)
        modality: Modality = baker.make(Modality)

        parking = {
            "license": "fjdj5678912",
            "chassis": "438743875378",
            "renavam": "745783475",
            "axle": 2,
            "year": 2021,
            "gross_weight": 1000,
            "vehicle_type": "TRACIONADORA",
            "body": body.id,
            "modality": modality.id,
        }

        response = APIClient().post(
            url,
            {
                "license": parking["license"],
                "chassis": parking["chassis"],
                "renavam": parking["renavam"],
                "axle": parking["axle"],
                "year": parking["year"],
                "gross_weight": parking["gross_weight"],
                "vehicle_type": parking["vehicle_type"],
                "body": str(uuid.uuid4()),
                "modality": str(uuid.uuid4()),
            },
        )

        assert response.status_code == 400

        response_data = response.json()
        assert "body" in response_data
        assert "modality" in response_data

        assert "objeto não existe." in response_data["body"][0]
        assert "objeto não existe." in response_data["modality"][0]
