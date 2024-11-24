import json
from io import BytesIO

import pytest
from django.core.files.base import ContentFile
from model_bakery import baker
from PIL import Image

from core.company.infra.company_django_app.models import Contract
from core.company.infra.company_django_app.serializers import ContractListSerializer


def generate_test_document() -> ContentFile:
    image = BytesIO()
    img = Image.new("RGB", (100, 100), color="red")
    img.save(image, format="PNG")
    image.seek(0)
    return ContentFile(image.read(), name="test_avatar.png")


@pytest.mark.django_db
class TestContractListSerializer:
    def test_list_serializer_with_many_contracts(self) -> None:
        avatar_document = baker.make(
            "Document",
            file=generate_test_document(),
        )
        contracts = baker.make(
            Contract,
            _quantity=3,
            source_company__avatar=avatar_document,
            target_company__avatar=avatar_document,
        )
        serializer = ContractListSerializer(contracts, many=True)
        assert len(serializer.data) == 3
        print(json.dumps(serializer.data, indent=2))
        assert serializer.data == [
            {
                "id": str(contract.id),
                "source_company": {
                    "id": str(contract.source_company.id),
                    "name": contract.source_company.name,
                    "avatar": (
                        f"http://localhost:8000{contract.source_company.avatar.file.url}"
                    ),
                },
                "target_company": {
                    "id": str(contract.target_company.id),
                    "name": contract.target_company.name,
                    "avatar": (
                        f"http://localhost:8000{contract.target_company.avatar.file.url}"
                    ),
                },
                "contract_type": contract.contract_type,
            }
            for contract in contracts
        ]

    def test_list_serializer_with_no_contracts(self) -> None:
        contracts = []
        serializer = ContractListSerializer(contracts, many=True)
        assert serializer.data == []

    def test_retrieve_serializer_with_a_specific_contract(self) -> None:
        avatar_document = baker.make(
            "Document",
            file=generate_test_document(),
        )
        contract = baker.make(
            Contract,
            source_company__avatar=avatar_document,
            target_company__avatar=avatar_document,
        )
        serializer = ContractListSerializer(contract)

        assert serializer.data == {
            "id": str(contract.id),
            "source_company": {
                "id": str(contract.source_company.id),
                "name": contract.source_company.name,
                "avatar": (
                    f"http://localhost:8000{contract.source_company.avatar.file.url}"
                ),
            },
            "target_company": {
                "id": str(contract.target_company.id),
                "name": contract.target_company.name,
                "avatar": (
                    f"http://localhost:8000{contract.source_company.avatar.file.url}"
                ),
            },
            "contract_type": contract.contract_type,
        }

    def test_retrieve_serializer_with_no_contract(self) -> None:
        contract = {}
        serializer = ContractListSerializer(contract)
        assert serializer.data == {}
