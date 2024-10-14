# from dataclasses import dataclass
import json

# from uuid import UUID, uuid4
# from django.test import override_settings
# from django.urls import reverse
from model_bakery import baker
import pytest

# from rest_framework import status
from rest_framework.test import APIClient
from core.company.infra.django_app.models import Company


# @dataclass
# class Company:
#     id: UUID
#     name: str
#     trade_name: str


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
        baker.make(Company, _quantity=3)

        url = "/api/companies/"
        response = APIClient().get(url)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3
        # response = APIClient().get(url)

        # expected_data = {
        #     "data": [
        #         {
        #             "id": str(category_documentary.id),
        #             "name": "Documentary",
        #             "description": "Documentary description",
        #             "is_active": True,
        #         },
        #         {
        #             "id": str(category_movie.id),
        #             "name": "Movie",
        #             "description": "Movie description",
        #             "is_active": True,
        #         },
        #     ],
        #     "meta": {
        #         "current_page": 1,
        #         "per_page": DEFAULT_PAGINATION_SIZE,
        #         "total": 2,
        #     },
        # }

        # assert response.status_code == status.HTTP_200_OK
        # assert response.data == expected_data
