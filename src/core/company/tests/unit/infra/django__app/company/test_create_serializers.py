import uuid

import pytest
from model_bakery import baker
from pycpfcnpj import gen

from core.company.infra.company_django_app.serializers import CompanyCreateSerializer
from core.uploader.infra.uploader_django_app.models import Document


@pytest.mark.django_db
class TestCompanyCreateSerializer:
    def test_create_serializer_with_valid_data(self) -> None:
        cnpj = gen.cnpj()
        document = baker.make(Document, file="th.jpg", attachment_key=uuid.uuid4)
        data = {
            "name": "Company",
            "person_type": "PJ",
            "document_number": cnpj,
            "documents_attachment_keys": [str(document.attachment_key)],
            "is_active": True,
        }
        serializer = CompanyCreateSerializer(data=data)
        if not serializer.is_valid():
            print(serializer.errors)

        assert serializer.is_valid() is True

    def test_create_serializer_with_invalid_data(self) -> None:
        data = {
            "name": "Company",
            "trade_name": "Company Trade",
            "document_number": "12345678901234",
            "person_type": "Pessoa Jurídica",
            "is_active": "verdadeiro",
        }
        serializer = CompanyCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert "Must be a valid boolean." in serializer.errors["is_active"]
        assert (
            f'"{data["person_type"]}" não é um escolha válido.'
            in serializer.errors["person_type"]
        )

    def test_if_a_new_uuid_is_generated_with_more_companies(self) -> None:
        cnpj = gen.cnpj()
        cpf = gen.cpf()
        companies = [
            {
                "name": "Company 1",
                "trade_name": "Trade Name 1",
                "person_type": "PJ",
                "is_active": True,
                "document_number": cnpj,
            },
            {
                "name": "Company 2",
                "trade_name": "Trade Name 2",
                "person_type": "PF",
                "is_active": True,
                "document_number": cpf,
            },
        ]

        serializer = CompanyCreateSerializer(data=companies[0])
        assert serializer.is_valid() is True
        company1 = serializer.save()
        assert company1.id is not None

        serializer = CompanyCreateSerializer(data=companies[1])
        assert serializer.is_valid() is True
        company2 = serializer.save()

        assert company2.id is not None
        assert company1.id != company2.id
