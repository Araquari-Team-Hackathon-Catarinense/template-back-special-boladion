import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.vehicle.infra.vehicle_django_app.models import (
    Composition,
    Vehicle,
    VehicleComposition,
)
from django_project.settings import API_VERSION


@pytest.mark.django_db
class TestVehicleDetailAPI:
    def test_detail_vehicle_composition(self) -> None:
        vehicle = baker.make(Vehicle, license="ABC1234")
        composition = baker.make(Composition)

        vehicle_composition = baker.make(
            VehicleComposition, vehicle=vehicle, composition=composition, sequence=1
        )

        url = f"/api/{API_VERSION}/vehicle/get-vehicle-composition/?license={vehicle.license}"

        client = APIClient()

        response = client.get(url)

        assert (
            response.status_code == 200
        ), f"Esperado 200 OK, mas obtido {response.status_code}."

        response_data = response.json()
