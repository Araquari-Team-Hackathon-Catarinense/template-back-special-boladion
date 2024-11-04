import pytest
from model_bakery import baker

from core.company.infra.company_django_app.models import Company
from core.company.infra.company_django_app.serializers import CompanyListSerializer
from django_project.settings import BASE_URL


@pytest.mark.django_db
class TestCompanyListSerializer:
    def test_list_serializer_with_many_companies(self) -> None:
        companies = baker.make(Company, _quantity=3, name="Company")
        serializer = CompanyListSerializer(companies, many=True)
        assert serializer.data == [
            {
                "id": str(company.id),
                "name": company.name,
                "trade_name": company.trade_name,
                "person_type": company.person_type,
                "document_number": company.document_number,
                "address": company.address,
                "is_active": company.is_active,
                "avatar": BASE_URL + company.avatar.url if company.avatar else None,
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
            "document_number": company.document_number,
            "address": company.address,
            "is_active": company.is_active,
            "avatar": BASE_URL + company.avatar.url if company.avatar else None,
        }
