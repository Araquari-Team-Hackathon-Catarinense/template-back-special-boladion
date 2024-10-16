import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import Parking


@pytest.mark.django_db
class TestRetrieveParkingAPI:
    def test_retrieve_a_valid_parking(self) -> None:
        company: Company = baker.make(Company)

        parking: Parking = baker.make(Parking, entity=company, slots=0)

        url = f"/api/parkings/{str(parking.id)}/"
        response = APIClient().get(url)

        expected_data = {
            "id": str(parking.id),
            "description": parking.description,
            "slots": parking.slots,
            "entity": str(parking.entity.id),
            "sectors": [],
        }
        assert response.status_code == 200
        assert json.loads(response.content) == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_parking(self) -> None:
        url = "/api/parkings/12345678-1234-1234-1234-123456789012/"
        response = APIClient().get(url)
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Parking matches the given query."
        }
