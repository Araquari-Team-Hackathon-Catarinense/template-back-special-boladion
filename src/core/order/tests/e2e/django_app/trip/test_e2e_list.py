import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.order.infra.order_django_app.models import TransportContract, Trip
from core.user.infra.user_django_app.models import Driver
from core.vehicle.infra.vehicle_django_app.models import Composition


@pytest.mark.django_db
class TestListTripAPI:
    def test_list_trips(self):
        company = baker.make(Company)
        transport_contract = baker.make(
            TransportContract, company=company, balance=1000.0, quantity=10.0
        )
        driver = baker.make(Driver)
        composition = baker.make(Composition)

        url = "/api/trips/"
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}

        trips = baker.make(
            Trip,
            transport_contract=transport_contract,
            driver=driver,
            vehicle=composition,
            quantity=1.0,
            _quantity=3,
        )

        print(trips)

        assert Trip.objects.count() == 3

        response = APIClient().get(url, **headers)
        assert response.status_code == 200

        response_data = response.json()
        assert response_data["total"] == len(trips)
        assert len(response_data["results"]) == len(trips)
