import pytest
from model_bakery import baker
from pycpfcnpj import gen

from core import company
from core.company.infra.company_django_app.models import Company
from core.company.infra.company_django_app.serializers import EmployeeCreateSerializer
from core.user.infra.user_django_app.models import User
from core.user.infra.user_django_app.serializers import UserCreateSerializer


@pytest.mark.django_db
class TestEmployeeCreateSerializer:
    def test_create_serializer_with_valid_data(self) -> None:
        company = baker.make(Company)
        user = baker.make(User)

        data = {"company": company.id, "user": user.id, "is_active": True}

        serializer = EmployeeCreateSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_serializer_with_invalid_data(self) -> None:
        data = {"company": 1, "user": 1, "is_active": "invalid"}
        serializer = EmployeeCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert "Must be a valid boolean." in serializer.errors["is_active"]
        assert 'Pk inválido "1" - objeto não existe.' in serializer.errors["company"]
        assert 'Pk inválido "1" - objeto não existe.' in serializer.errors["user"]

    def test_create_serializer_with_more_employees(self) -> None:
        company = baker.make(Company)
        user = baker.make(User)

        employees = [
            {"company": company.id, "user": user.id, "is_active": True},
            {"company": company.id, "user": user.id, "is_active": True},
        ]

        serializer = EmployeeCreateSerializer(data=employees[0])
        assert serializer.is_valid() is True

        employee1 = serializer.save()
        assert employee1.id is not None

        serializer = EmployeeCreateSerializer(data=employees[1])
        assert serializer.is_valid() is True

        employee2 = serializer.save()
        assert employee2.id is not None

        assert employee1.id != employee2.id
