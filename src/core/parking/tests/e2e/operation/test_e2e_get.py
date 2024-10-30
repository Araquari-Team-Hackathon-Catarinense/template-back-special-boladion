import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import Operation, Parking

url = "/api/operations/"


@pytest.mark.django_db
class TestOperationListAPI:
    def test_list_operation(self) -> None:
        # Criação de dados para o teste
        company: Company = baker.make(Company)
        parking: Parking = baker.make(Parking, company=company)
        created_operations = baker.make(
            Operation, _quantity=3, parking=parking
        )  # Note a mudança de `created_operation` para `created_operations`

        # Define a URL correta para a API
        url = "/api/operations/"  # Substitua pelo endpoint correto

        # Cabeçalho da requisição
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}

        # Faz a requisição GET
        response = APIClient().get(url, **headers)

        # Prepara os dados esperados
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
                    "id": str(operation.id),
                    "name": operation.name,
                }
                for operation in created_operations
            ],
        }

        # Verificações
        assert response.status_code == 200
        assert len(response.json()["results"]) == 3
        assert response.json() == expected_data
