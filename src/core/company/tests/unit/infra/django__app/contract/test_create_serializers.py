import pytest
from model_bakery import baker

from core.company.infra.company_django_app.models import Company
from core.company.infra.company_django_app.serializers import ContractCreateSerializer, EmployeeCreateSerializer


@pytest.mark.django_db
class TestContractCreateSerializer:
    def test_create_serializer_with_valid_data(self) -> None:
        source_company = baker.make(Company)
        target_company = baker.make(Company)

        data = {
            "source_company": str(source_company.id),
            "target_company": str(target_company.id),
            "contract_type": "CLIENTE"
        }

        serializer = ContractCreateSerializer(data=data)
        assert serializer.is_valid() is True

    def test_if_throw_error_when_create_serializer_with_invalid_data(self) -> None:
        data = {"source_company": 1, "target_company": 1, "contract_type": "invalid"}
        serializer = ContractCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert 'Pk inválido "1" - objeto não existe.' in serializer.errors["source_company"]
        assert 'Pk inválido "1" - objeto não existe.' in serializer.errors["target_company"]
        assert '"invalid" não é um escolha válido.' in serializer.errors["contract_type"]

    def test_if_throw_error_when_create_serializer_with_no_contract_type(self) -> None:
        source_company = baker.make(Company)
        target_company = baker.make(Company)

        data = {
            "source_company": str(source_company.id),
            "target_company": str(target_company.id),
        }

        serializer = ContractCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert "Este campo é obrigatório." in serializer.errors["contract_type"]
