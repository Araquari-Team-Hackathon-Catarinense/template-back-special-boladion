import pytest
from model_bakery import baker
from pycpfcnpj import gen

from core.user.infra.user_django_app.models import User
from core.user.infra.user_django_app.serializers import UserDetailSerializer


@pytest.mark.django_db
class TestUserDetailSerializer:
    def test_retrieve_serializer_with_an_specific_user(self) -> None:
        user = baker.make(User, cpf=gen.cpf())
        serializer = UserDetailSerializer(user)

        print(serializer)

        expected_data = {
            "id": str(user.id),
            "email": user.email,
            "name": user.name,
            "cpf": user.cpf,
            "document_number": user.document_number,
            "is_active": user.is_active,
            "date_joined": user.date_joined.isoformat() if user.date_joined else None,
            "last_login": user.last_login.isoformat() if user.last_login else None,
        }

        assert serializer.data == expected_data

    def test_list_serializer_with_no_user(self) -> None:
        user = {}
        serializer = UserDetailSerializer(user)
        assert serializer.data == {}
