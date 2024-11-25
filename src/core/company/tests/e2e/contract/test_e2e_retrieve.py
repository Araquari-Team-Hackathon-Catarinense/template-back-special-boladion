import json
from io import BytesIO

import pytest
from django.core.files.base import ContentFile
from model_bakery import baker
from PIL import Image
from rest_framework.test import APIClient

from core.company.infra.company_django_app.models import Contract
from django_project.settings import API_VERSION


def generate_test_document() -> ContentFile:
    # Gerar um arquivo de imagem em memória
    image = BytesIO()
    img = Image.new("RGB", (100, 100), color="red")
    img.save(image, format="PNG")
    image.seek(0)
    return ContentFile(image.read(), "test_avatar.png")


@pytest.mark.django_db
class TestRetrieveAPI:
    def test_retrieve_a_valid_contract(self) -> None:

        avatar_document = baker.make(
            "Document",
            file=generate_test_document(),
        )

        contracts = baker.make(
            "Contract",
            _quantity=3,
            source_company__avatar=avatar_document,
            target_company__avatar=avatar_document,
        )

        company = contracts[0].source_company
        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        url = f"/api/{API_VERSION}/company/contracts/{contracts[0].id}/"
        response = APIClient().get(url, **headers)

        expected_data = {
            "id": str(contracts[0].id),
            "source_company": {
                "id": str(contracts[0].source_company.id),
                "name": contracts[0].source_company.name,
                "avatar": (
                    f"http://localhost:8000{contracts[0].source_company.avatar.file.url}"
                ),
            },
            "target_company": {
                "id": str(contracts[0].target_company.id),
                "name": contracts[0].target_company.name,
                "avatar": (
                    f"http://localhost:8000{contracts[0].target_company.avatar.file.url}"
                ),
            },
            "contract_type": contracts[0].contract_type,
        }

        assert response.status_code == 200
        assert response.json() == expected_data

    def test_if_throw_error_when_retrieving_an_invalid_contract(self) -> None:
        contracts = baker.make(Contract, _quantity=3)
        company = contracts[0].source_company

        headers = {"HTTP_X_COMPANY_ID": str(company.id)}
        url = f"/api/{API_VERSION}/company/contracts/12345678-1234-1234-1234-123456789012/"

        response = APIClient().get(url, **headers)
        assert response.status_code == 404
        assert json.loads(response.content) == {
            "detail": "No Contract matches the given query."
        }
