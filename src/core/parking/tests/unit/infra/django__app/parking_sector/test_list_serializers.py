import pytest
from model_bakery import baker
from pycpfcnpj import gen

from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import Parking, ParkingSector
from core.parking.infra.parking_django_app.serializers import (
    ParkingSectorListSerializer,
)


@pytest.mark.django_db
class TestParkingSectorListSerializer:
    def test_list_serializer_with_many_parking_sectors(self) -> None:
        cnpj = gen.cnpj()
        company: Company = Company.objects.create(
            name="Company",
            person_type="PJ",
            document_number=cnpj,
        )
        parking: Parking = Parking.objects.create(
            description="Meu Estacionamento",
            company=company,
        )
        parking_sectors = baker.make(
            ParkingSector, _quantity=3, parking=parking, sector_type="ROTATIVE"
        )
        serializer = ParkingSectorListSerializer(parking_sectors, many=True)
        assert serializer.data == [
            {
                "id": str(parking_sector.id),
                "description": parking_sector.description,
                "qty_slots": parking_sector.qty_slots,
                "sector_type": parking_sector.sector_type,
                "contract": None,
            }
            for parking_sector in parking_sectors
        ]

    def test_list_serializer_with_no_parking_sectors(self) -> None:
        parking_sectors = []
        serializer = ParkingSectorListSerializer(parking_sectors, many=True)
        assert serializer.data == []

    def test_list_serializer_with_one_parking(self) -> None:
        company = Company.objects.create(
            name="Company",
            person_type="PJ",
            document_number=gen.cnpj(),
        )
        parking: Parking = Parking.objects.create(
            description="Meu Estacionamento",
            company=company,
        )
        parking_sector = baker.make(
            ParkingSector, parking=parking, sector_type="ROTATIVE"
        )
        serializer = ParkingSectorListSerializer(parking_sector, many=False)
        assert serializer.data == {
            "id": str(parking_sector.id),
            "description": parking_sector.description,
            "qty_slots": parking_sector.qty_slots,
            "sector_type": parking_sector.sector_type,
            "contract": None,
        }
