from datetime import date

import pytest
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.order.infra.order_django_app.models import (
    Composition,
    TransportContract,
    Trip,
)
from core.user.infra.user_django_app.models import Driver

url = "/api/trips/"


@pytest.mark.django_db
class TestCreateTripContractAPITest:
    def test_create_valid_trip(self):
        company = baker.make(Company)
        driver = baker.make(Driver, valid_until_license=date(2030, 10, 10))

        composition = baker.make(Composition)
        transport_contract = baker.make(
            TransportContract, company=company, balance=1000.0, quantity=10.0
        )

        trip = baker.make(
            Trip,
            driver=driver,
            vehicle=composition,
            transport_contract=transport_contract,
            quantity=lambda: 1.0,
        )

        operation_data = {
            "transport_contract": str(transport_contract.id),
            "quantity": 1.0,
            "date": "2021-10-10",
            "order_number": "123",
            "vehicle": str(composition.id),
            "driver": str(driver.id),
        }

        headers = {"HTTP_X_COMPANY_ID": str(company.id)}

        response = APIClient().post(
            url,
            operation_data,
            format="json",
            **headers,
        )
        print("Response Data:", response.json())
        assert response.status_code == status.HTTP_201_CREATED

        # Assertions
        assert Trip.objects.filter(transport_contract=transport_contract).exists()
        assert Trip.objects.filter(order_number="123").exists()
        assert Trip.objects.filter(quantity=1.0).exists()
        assert Trip.objects.filter(date="2021-10-10").exists()
        assert Trip.objects.filter(vehicle=composition).exists()
        assert Trip.objects.filter(driver=driver).exists()
