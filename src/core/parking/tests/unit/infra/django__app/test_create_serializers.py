from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.serializers import ParkingCreateSerializer

from pycpfcnpj import gen
import pytest


@pytest.mark.django_db
class TestParkingCreateSerializer:
    def test_create_serializer_with_valid_data(self) -> None:
        cnpj = gen.cnpj()
        company = Company.objects.create(
            name="Company",
            person_type="PJ",
            document_number=cnpj,
        )
        data = {
            "description": "Meu Estacionamento",
            "entity": company.id,
        }
        serializer = ParkingCreateSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_serializer_with_invalid_data(self) -> None:
        entity_id = "912927c3-2ee5-4d31-b1d8-f6a5838c56cc"
        data = {
            "description": "Meu Estacionamento",
            "entity": "912927c3-2ee5-4d31-b1d8-f6a5838c56cc",
        }
        serializer = ParkingCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert f'Invalid pk "{entity_id}" - object does not exist.' in serializer.errors["entity"]

    def test_if_a_new_uuid_is_generated_with_more_parkings(self) -> None:
        cnpj = gen.cnpj()
        company = Company.objects.create(
            name="Company",
            person_type="PJ",
            document_number=cnpj,
        )
        parkings = [
            {
                "description": "Meu Estacionamento",
                "entity": company.id,
            },
            {
                "description": "Meu Estacionamento 2",
                "entity": company.id,
            },
        ]

        serializer = ParkingCreateSerializer(data=parkings[0])
        assert serializer.is_valid() is True
        parking1 = serializer.save()
        assert parking1.id is not None

        serializer = ParkingCreateSerializer(data=parkings[1])
        assert serializer.is_valid() is True
        parking2 = serializer.save()

        assert parking2.id is not None
        assert parking1.id != parking2.id
