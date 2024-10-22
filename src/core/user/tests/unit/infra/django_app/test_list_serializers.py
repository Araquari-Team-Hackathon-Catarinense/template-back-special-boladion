import pytest
from model_bakery import baker
from pycpfcnpj import gen

from core.user.infra.user_django_app.models import User
from core.user.infra.user_django_app.serializers import UserListSerializer


@pytest.mark.django_db
class TestUserListSerializer:
    def test_list_serializer_with_many_users(self) -> None:
        unique_cpfs = set()
        users = []

        while len(users) < 5:
            cpf = gen.cpf()
            if cpf not in unique_cpfs:
                unique_cpfs.add(cpf)
                users.append(baker.make(User, cpf=cpf))

        serializer = UserListSerializer(users, many=True)

        assert serializer.data == [
            {
                "id": user.id,
                "name": user.name,
                "cpf": user.cpf,
                "address": user.address,
                "email": user.email,
            }
            for user in users
        ]

    def test_list_serializer_with_one_user(self) -> None:
        user = baker.make(User, cpf=gen.cpf())
        serializer = UserListSerializer(user, many=False)
        assert serializer.data == {
            "id": user.id,
            "name": user.name,
            "cpf": user.cpf,
            "address": user.address,
            "email": user.email,
        }
