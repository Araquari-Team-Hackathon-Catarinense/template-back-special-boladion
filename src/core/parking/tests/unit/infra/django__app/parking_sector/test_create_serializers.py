import pytest
from model_bakery import baker
from pycpfcnpj import gen

from core.company.infra.company_django_app.models import Company, Contract
from core.parking.infra.parking_django_app.models import Parking
from core.parking.infra.parking_django_app.serializers import (
    ParkingSectorCreateSerializer,
)


@pytest.mark.django_db
class TestParkingCreateSerializer:
    def test_create_serializer_with_valid_data_of_sector_type_contract(self) -> None:
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
        contract: Contract = baker.make(Contract)
        data = {
            "description": "Meu Setor de Estacionamento",
            "qty_slots": 10,
            "sector_type": "CONTRACT",
            "parking": parking.id,
            "contract": contract.id,
        }
        serializer = ParkingSectorCreateSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_serializer_with_valid_data_of_sector_type_rotative(self) -> None:
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
        data = {
            "description": "Meu Setor de Estacionamento",
            "qty_slots": 10,
            "sector_type": "ROTATIVE",
            "parking": parking.id,
        }
        serializer = ParkingSectorCreateSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_serializer_with_invalid_data(self) -> None:
        parking_id = "11111111-2ee5-4d31-b1d8-f6a5838c56cc"
        data = {
            "description": "Meu Setor de Estacionamento",
            "qty_slots": 10,
            "sector_type": "ROTATIVE",
            "parking": parking_id,
        }
        serializer = ParkingSectorCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert (
            f'Pk inválido "{parking_id}" - objeto não existe.'
            in serializer.errors["parking"]
        )

    def test_create_serializer_with_invalid_data_of_sector_type_contract(self) -> None:
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
        data = {
            "description": "Meu Setor de Estacionamento",
            "qty_slots": 10,
            "sector_type": "CONTRACT",
            "parking": parking.id,
        }
        serializer = ParkingSectorCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert "Contract is required" in serializer.errors["non_field_errors"][0]

    def test_if_a_new_uuid_is_generated_with_more_parking_sectors(self) -> None:
        cnpj = gen.cnpj()
        company = Company.objects.create(
            name="Company",
            person_type="PJ",
            document_number=cnpj,
        )
        parking: Parking = Parking.objects.create(
            description="Meu Estacionamento",
            company=company,
        )
        parking_sectors = [
            {
                "description": "Meu Setor de Estacionamento 1",
                "qty_slots": 10,
                "sector_type": "ROTATIVE",
                "parking": parking.id,
            },
            {
                "description": "Meu Setor de Estacionamento 2",
                "qty_slots": 10,
                "sector_type": "ROTATIVE",
                "parking": parking.id,
            },
        ]

        serializer = ParkingSectorCreateSerializer(data=parking_sectors[0])
        assert serializer.is_valid() is True
        parking_sector_1 = serializer.save()
        assert parking_sector_1.id is not None

        serializer = ParkingSectorCreateSerializer(data=parking_sectors[1])
        assert serializer.is_valid() is True
        parking_sector_2 = serializer.save()

        assert parking_sector_2.id is not None
        assert parking_sector_1.id != parking_sector_2.id
