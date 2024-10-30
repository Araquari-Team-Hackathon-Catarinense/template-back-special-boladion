import pytest
from model_bakery import baker

from core.vehicle.infra.vehicle_django_app.models import Modality
from core.vehicle.infra.vehicle_django_app.views import ModalityListSerializer


@pytest.mark.django_db
class TestModalityListSerializer:
    def test_list_serializer_with_many_modalities(self) -> None:
        modalities = baker.make(Modality, _quantity=3)

        serializer = ModalityListSerializer(modalities, many=True)
        assert serializer.data == [
            {
                "id": str(modality.id),
                "description": modality.description,
                "axle": modality.axle,
            }
            for modality in modalities
        ]

    def test_list_serializer_with_no_modalities(self) -> None:
        modality = []
        serializer = ModalityListSerializer(modality, many=True)
        assert serializer.data == []

    def test_list_serializer_with_one_modality(self) -> None:
        modality: Modality = baker.make(Modality)
        serializer = ModalityListSerializer(modality, many=False)
        assert serializer.data == {
            "id": str(modality.id),
            "description": modality.description,
            "axle": modality.axle,
        }
