import pytest
from model_bakery import baker
from pycpfcnpj import gen

from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import Parking
from core.parking.infra.parking_django_app.serializers import ParkingListSerializer


@pytest.mark.django_db
class TestParkingListSerializer:
    def test_list_serializer_with_many_parkings(self) -> None:
        company = Company.objects.create(
            name="Company",
            person_type="PJ",
            document_number=gen.cnpj(),
        )
        parkings = baker.make(Parking, _quantity=3, company=company)
        serializer = ParkingListSerializer(parkings, many=True)
        assert serializer.data == [
            {
                "id": str(parking.id),
                "company": str(parking.company.id),
                "description": parking.description,
                "slots": parking.slots,
            }
            for parking in parkings
        ]

    def test_list_serializer_with_no_parkings(self) -> None:
        parkings = []
        serializer = ParkingListSerializer(parkings, many=True)
        assert serializer.data == []

    def test_list_serializer_with_one_parking(self) -> None:
        company = Company.objects.create(
            name="Company",
            person_type="PJ",
            document_number=gen.cnpj(),
        )
        parking = baker.make(Parking, company=company)
        serializer = ParkingListSerializer(parking, many=False)
        assert serializer.data == {
            "id": str(parking.id),
            "company": str(parking.company.id),
            "description": parking.description,
            "slots": parking.slots,
        }
