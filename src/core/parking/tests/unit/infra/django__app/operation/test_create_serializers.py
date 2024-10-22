import pytest
from model_bakery import baker

from core.parking.infra.parking_django_app.models import Operation, Parking
from core.parking.infra.parking_django_app.serializers import OperationCreateSerializer


@pytest.mark.django_db
class TestOperationCreateSerializer:
    def test_create_serializer_with_valid_operation(self) -> None:
        parking: Parking = baker.make(Parking)

        data = {
            "name": "My Operation",
            "parking": parking.id,
        }
        serializer = OperationCreateSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_serializer_with_invalid_data(self) -> None:
        parking_id = "11111111-2ee5-4d31-b1d8-f6a5838c56cc"
        data = {
            "name": "My Operation",
            "parking": parking_id,
        }
        serializer = OperationCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert (
            f'Invalid pk "{parking_id}" - object does not exist.'
            in serializer.errors["parking"]
        )

    def test_create_serializer_dont_passing_parking(self) -> None:
        data = {
            "name": "My Operation",
        }
        serializer = OperationCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert "This field is required." in serializer.errors["parking"][0]
