import uuid

import pytest
from model_bakery import baker
from pycpfcnpj import gen

from core.user.infra.user_django_app.models import User
from core.user.infra.user_django_app.serializers import UserListSerializer


@pytest.mark.django_db
class TestUserListSerializer:
    def test_list_serializer_with_many_users(self) -> None:
        users = baker.make(User, _quantity=3)

        serializer = UserListSerializer(users, many=True)

        assert serializer.data == [
            {
                "id": str(user.id),
                "email": user.email,
                "name": user.name,
                "cpf": user.cpf,
                "address": user.address,
                "avatar": None,
            }
            for user in users
        ]

    def test_list_serializer_with_one_user(self) -> None:
        user = baker.make(User, cpf=gen.cpf())
        serializer = UserListSerializer(user, many=False)
        assert serializer.data == {
            "id": str(user.id),
            "name": user.name,
            "cpf": user.cpf,
            "address": user.address,
            "email": user.email,
            "avatar": None,
        }
