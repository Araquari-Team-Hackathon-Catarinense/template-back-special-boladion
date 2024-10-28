import pytest
from model_bakery import baker

from core.vehicle.infra.vehicle_django_app.models import Body
from core.vehicle.infra.vehicle_django_app.views import (
    BodyCreateSerializer,
    BodyListSerializer,
)


@pytest.mark.django_db
class TestBodyListSerializer:
    def test_list_serializer_with_many_bodies(self) -> None:
        bodies = baker.make(Body, _quantity=3)

        serializer = BodyListSerializer(bodies, many=True)
        assert serializer.data == [
            {
                "id": str(body.id),
                "description": body.description,
            }
            for body in bodies
        ]

    def test_list_serializer_with_no_bodies(self) -> None:
        body = []
        serializer = BodyListSerializer(body, many=True)
        assert serializer.data == []

    def test_list_serializer_with_one_body(self) -> None:
        body: Body = baker.make(Body)
        serializer = BodyListSerializer(body, many=False)
        assert serializer.data == {
            "id": str(body.id),
            "description": body.description,
        }
