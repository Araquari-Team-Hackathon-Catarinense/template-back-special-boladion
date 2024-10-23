import pytest
from model_bakery import baker

from core.company.infra.company_django_app.models import Contract
from core.company.infra.company_django_app.serializers import ContractListSerializer


@pytest.mark.django_db
class TestContractListSerializer:
    def test_list_serializer_with_many_contracts(self) -> None:
        contracts = baker.make(Contract, _quantity=3)
        serializer = ContractListSerializer(contracts, many=True)
        assert len(serializer.data) == 3
        assert serializer.data == [
            {
                "id": str(contract.id),
                "source_company": {
                    "id": str(contract.source_company.id),
                    "name": contract.source_company.name,
                },
                "target_company": {
                    "id": str(contract.target_company.id),
                    "name": contract.target_company.name,
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
        contract = baker.make(Contract)
        serializer = ContractListSerializer(contract)
        assert serializer.data ==  {
            "id": str(contract.id),
            "source_company": {
                "id": str(contract.source_company.id),
                "name": contract.source_company.name,
            },
            "target_company": {
                "id": str(contract.target_company.id),
                "name": contract.target_company.name,
            },
            "contract_type": contract.contract_type,
        }

    def test_retrieve_serializer_with_no_contract(self) -> None:
        contract = {}
        serializer = ContractListSerializer(contract)
        assert serializer.data == {}
