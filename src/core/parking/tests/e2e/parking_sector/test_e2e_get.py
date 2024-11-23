import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import Parking, ParkingSector


@pytest.mark.django_db
class TestParkingSectorListAPI:
    def test_list_parking_sectors(self) -> None:
        company: Company = baker.make(Company)
        parking: Parking = baker.make(Parking, company=company)
        created_parking_sectors = baker.make(
            ParkingSector, _quantity=3, parking=parking, sector_type="ROTATIVE"
        )
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}

        url = "/api/parking-sectors/"
        response = APIClient().get(url, **headers)

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
                    "id": str(parking_sector.id),
                    "description": parking_sector.description,
                    "sector_type": parking_sector.sector_type,
                    "qty_slots": parking_sector.qty_slots,
                    "parking": parking_sector.parking.description,
                    "contract": None,
                }
                for parking_sector in created_parking_sectors
            ],
        }

        assert response.status_code == 200
        assert len(response.json()["results"]) == 3
        assert json.loads(response.content) == expected_data
