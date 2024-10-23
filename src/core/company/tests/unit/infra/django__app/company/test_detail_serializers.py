import pytest
from attr.validators import instance_of
from model_bakery import baker
from pycpfcnpj import gen

from core.company.infra.company_django_app.models import Company
from core.company.infra.company_django_app.serializers import CompanyDetailSerializer


@pytest.mark.django_db
class TestCompanyDetailSerializer:
    def test_retrieve_serializer_with_a_specific_company(self) -> None:
        company = baker.make(Company, person_type="PF", document_number=gen.cpf())
        serializer = CompanyDetailSerializer(company)
        assert serializer.data == {
            "id": str(company.id),
            "name": company.name,
            "trade_name": company.trade_name,
            "person_type": company.person_type,
            "document_number": company.document_number,
            "is_active": company.is_active,
            "address": company.address,
            "contacts": company.contacts,
            "system_admin": company.system_admin,
            "document": company.document,
        }

    def test_list_serializer_with_no_company(self) -> None:
        company = {}
        serializer = CompanyDetailSerializer(company)
        assert serializer.data == {}
