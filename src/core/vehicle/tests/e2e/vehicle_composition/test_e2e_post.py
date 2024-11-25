import uuid

import pytest
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient

from core.vehicle.infra.vehicle_django_app.models import (
    Composition,
    Vehicle,
    VehicleType,
)
from django_project.settings import API_VERSION


@pytest.mark.django_db
class TestListAPI:
    def test_create_a_valid_vehicle_composition(self) -> None:
        url: str = f"/api/{API_VERSION}/vehicle/vehicle-composition/"

        vehicle = baker.make(Vehicle)
        composition = baker.make(Composition)

        response = APIClient().post(
            url,
            {
                "vehicle": str(vehicle.id),
                "composition": str(composition.id),
                "sequence": 1,
            },
        )

        print(response.json())
        assert response.status_code == 201

    def test_create_a_invalid_vehicle_composition(self) -> None:
        url: str = f"/api/{API_VERSION}/vehicle/vehicle-composition/"

        response = APIClient().post(
            url,
            {
                "vehicle": str(uuid.uuid4()),
                "composition": str(uuid.uuid4()),
                "sequence": 0,
            },
        )

        print(response.json())
        assert response.status_code == 400

    def test_create_with_invalid_vehicle_because_sequence_need_to_be_zero(self) -> None:
        url = f"/api/{API_VERSION}/vehicle/vehicle-composition/"

        vehicle = baker.make(Vehicle, vehicle_type=VehicleType.TRACIONADORA)
        composition = baker.make(Composition)

        response = APIClient().post(
            url,
            {
                "vehicle": str(vehicle.id),
                "composition": str(composition.id),
                "sequence": 1,
            },
        )

        assert response.status_code == 400

        response_data = response.json()
        print("Response Data:", response_data)

        # assert (
        #     "sequence" in response_data
        # ), "Chave 'sequence' não encontrada na resposta."

        assert (
            response_data["sequence"][0]
            == "A unidade tracionadora deve ter sequence igual a 0."
        )
