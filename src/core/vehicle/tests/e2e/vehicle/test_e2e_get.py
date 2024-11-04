import datetime
from datetime import datetime, timezone

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.vehicle.infra.vehicle_django_app.models import Vehicle


@pytest.mark.django_db
class TestVehicleDetailAPI:
    def test_detail_vehicle(self) -> None:
        vehicle: Vehicle = baker.make(
            Vehicle,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )

        url = f"/api/vehicles/{str(vehicle.id)}/"
        response = APIClient().get(url)

        # Extrair os dados de resposta JSON
        response_data = response.json()

        response_data["created_at"] = (
            datetime.fromisoformat(response_data["created_at"])
            .astimezone(timezone.utc)
            .isoformat()
        )
        response_data["updated_at"] = (
            datetime.fromisoformat(response_data["updated_at"])
            .astimezone(timezone.utc)
            .isoformat()
        )

        # Normalizar as datas em UTC
        expected_data = {
            "id": str(vehicle.id),
            "created_at": vehicle.created_at.astimezone(timezone.utc).isoformat(),
            "updated_at": (
                vehicle.updated_at.astimezone(timezone.utc).isoformat()
                if vehicle.updated_at
                else None
            ),
            "license": vehicle.license,
            "chassis": vehicle.chassis,
            "renavam": vehicle.renavam,
            "axle": vehicle.axle,
            "year": vehicle.year,
            "gross_weight": vehicle.gross_weight,
            "vehicle_type": vehicle.vehicle_type,
            "body": vehicle.body.id if vehicle.body else None,
            "modality": vehicle.modality.id if vehicle.modality else None,
            "documents": [],
        }

        # Verificar status da resposta
        assert response.status_code == 200

        # Comparar resposta e dados esperados
        assert response_data == expected_data
