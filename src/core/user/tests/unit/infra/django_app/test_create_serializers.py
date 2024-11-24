from datetime import datetime

import pytest
from pycpfcnpj import gen

from core.user.infra.user_django_app.serializers import UserCreateSerializer


@pytest.mark.django_db
class TestUserCreateSerializer:
    def test_create_serializer_with_valid_data(self) -> None:
        cpf = gen.cpf()
        data = {
            "name": "John Doe",
            "email": "johndoe@gmail.com",
            "cpf": cpf,
            "address": "Rua dos Bobos, nº 0",
            "password": "123456",
        }
        serializer = UserCreateSerializer(data=data)
        assert serializer.is_valid() is True

    def test_create_serializer_with_invalid_data(self) -> None:
        data = {
            "name": "John Doe",
            "email": None,
            "cpf": None,
            "address": "Rua dos Bobos, nº 0",
        }
        serializer = UserCreateSerializer(data=data)
        assert serializer.is_valid() is False
        assert "cpf" in serializer.errors
        cpf_errors = serializer.errors["cpf"]
        assert any("CPF inválido." in error.get("cpf", "") for error in cpf_errors)

    def test_create_serializer_with_one_more_user(self) -> None:
        cpf1 = gen.cpf()
        cpf2 = gen.cpf()

        while cpf1 == cpf2:
            cpf2 = gen.cpf()

        users = [
            {
                "name": "John Doe",
                "email": "johd@gmail.com",
                "cpf": cpf1,
                "address": "Rua dos Bobos, nº 0",
                "is_active": True,
                "date_joined": datetime.now(),
                "last_login": None,
                "password": "123456",
            },
            {
                "name": "Jane Doe",
                "email": "janedoe@gmail.com",
                "cpf": cpf2,
                "address": "Rua dos Bobos, nº 0",
                "is_active": True,
                "date_joined": datetime.now(),
                "last_login": None,
                "password": "123456",
            },
        ]

        serializer = UserCreateSerializer(data=users[0])
        assert serializer.is_valid() is True
        user1 = serializer.save()
        assert user1.id is not None

        serializer = UserCreateSerializer(data=users[1])
        assert serializer.is_valid() is True
        user2 = serializer.save()

        assert user1.id is not None
        assert user1.id != user2.id
