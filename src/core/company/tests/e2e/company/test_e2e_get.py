import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from django_project.settings import API_VERSION, BASE_URL


@pytest.mark.django_db
class TestListAPI:
    def test_list_companies(self) -> None:
        created_companies = baker.make(Company, _quantity=3, person_type="PJ")

        url = f"/api/{API_VERSION}/company/companies/"
        response = APIClient().get(url)

        expected_data = {
            "total": 3,
            "num_pages": 1,
            "page_number": 1,
            "page_size": 20,
            "links": {
                "next": None,
                "previous": None,
            },
            "results": [
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
                for company in created_companies
            ],
        }

        assert response.status_code == 200
        assert len(response.json()["results"]) == 3
        assert json.loads(response.content) == expected_data
