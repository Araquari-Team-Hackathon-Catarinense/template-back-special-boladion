import pytest
from attr.validators import instance_of
from model_bakery import baker
from pycpfcnpj import gen

from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import Parking
from core.parking.infra.parking_django_app.serializers import ParkingDetailSerializer


@pytest.mark.django_db
class TestParkingDetailSerializer:
    def test_retrieve_serializer_with_an_specific_parking(self) -> None:
        company = Company.objects.create(
            name="Company",
            person_type="PJ",
            document_number=gen.cnpj(),
        )
        parking = Parking.objects.create(
            description="Meu Estacionamento",
            company=company,
        )
        serializer = ParkingDetailSerializer(parking)
        assert serializer.data == {
            "id": str(parking.id),
            "company": str(parking.company.id),
            "description": parking.description,
            "slots": parking.slots,
            "sectors": [],
            "operations": [],
        }

    def test_list_serializer_with_no_parking(self) -> None:
        parking = {}
        serializer = ParkingDetailSerializer(parking)
        assert serializer.data == {}
