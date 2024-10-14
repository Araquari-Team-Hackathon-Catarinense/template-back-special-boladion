from core.company.infra.django_app.models import Company
from core.company.infra.django_app.serializers import (
    CompanyCreateSerializer,
    CompanyListSerializer,
)
from model_bakery import baker
import pytest


@pytest.mark.django_db
class TestCompanyListSerializer:
    def test_list_serializer_with_many_companies(self) -> None:
        companies = baker.make(Company, _quantity=3)
        serializer = CompanyListSerializer(companies, many=True)
        assert serializer.data == [
            {
                "id": str(company.id),
                "name": company.name,
                "trade_name": company.trade_name,
                "person_type": company.person_type,
                "is_active": company.is_active,
            }
            for company in companies
        ]

    def test_list_serializer_with_no_companies(self) -> None:
        companies = []
        serializer = CompanyListSerializer(companies, many=True)
        assert serializer.data == []

    def test_list_serializer_with_one_company(self) -> None:
        company = baker.make(Company)
        serializer = CompanyListSerializer(company, many=False)
        assert serializer.data == {
            "id": str(company.id),
            "name": company.name,
            "trade_name": company.trade_name,
            "person_type": company.person_type,
            "is_active": company.is_active,
        }


@pytest.mark.django_db
class TestCompanyCreateSerializer:
    def test_create_serializer_with_valid_data(self) -> None:
        data = {
            "name": "Company",
            "person_type": "PJ",
            "document_number": "12345678901234",
        }
        serializer = CompanyCreateSerializer(data=data)
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
            f'"{data["person_type"]}" is not a valid choice.'
            in serializer.errors["person_type"]
        )
