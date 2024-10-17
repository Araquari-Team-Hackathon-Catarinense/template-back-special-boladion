import pytest
from model_bakery import baker

from core.parking.infra.parking_django_app.models import Operation, Parking
from core.parking.infra.parking_django_app.serializers import OperationListSerializer


@pytest.mark.django_db
class TestParkingSectorListSerializer:
    def test_list_serializer_with_many_operations(self) -> None:
        parking: Parking = baker.make(Parking)

        operations = baker.make(Operation, parking=parking, _quantity=3)

        serializer = OperationListSerializer(operations, many=True)
        assert serializer.data == [
            {
                "id": str(operation.id),
                "name": operation.name,
            }
            for operation in operations
        ]

    def test_list_serializer_with_no_operation(self) -> None:
        operation = []
        serializer = OperationListSerializer(operation, many=True)
        assert serializer.data == []

    def test_list_serializer_with_one_parking(self) -> None:
        parking: Parking = baker.make(Parking)

        operation: Operation = baker.make(Operation, parking=parking)
        serializer = OperationListSerializer(operation, many=False)
        assert serializer.data == {
            "id": str(operation.id),
            "name": operation.name,
        }
