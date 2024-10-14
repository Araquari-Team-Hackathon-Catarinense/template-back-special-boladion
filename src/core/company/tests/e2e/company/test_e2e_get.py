import json
from model_bakery import baker
import pytest
from rest_framework.test import APIClient

from core.company.infra.django_app.models import Company


# @pytest.fixture
# def company_item():
#     return {"id": ""}


# @pytest.fixture
# def category_documentary():
#     return Category(
#         name="Documentary",
#         description="Documentary description",
#     )


# @pytest.fixture
# def category_repository() -> DjangoORMCategoryRepository:
#     return DjangoORMCategoryRepository()


@pytest.mark.django_db
class TestListAPI:
    def test_list_categories(self) -> None:
        created_companies = baker.make(Company, _quantity=3)

        url = "/api/companies/"
        response = APIClient().get(url)

        expected_data = [
            {
                "id": str(company.id),
                "name": company.name,
                "trade_name": company.trade_name,
                "person_type": company.person_type,
                "is_active": company.is_active,
            }
            for company in created_companies
        ]

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3
        assert json.loads(response.content) == expected_data
