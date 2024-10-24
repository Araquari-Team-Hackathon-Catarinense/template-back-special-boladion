from datetime import datetime, timedelta, timezone

import pytest
from model_bakery import baker
from pycpfcnpj import gen

from core.user.infra.user_django_app.models import User
from core.user.infra.user_django_app.serializers import UserDetailSerializer


@pytest.mark.django_db
class TestUserDetailSerializer:
    def test_retrieve_serializer_with_a_specific_user(self) -> None:

        time_zone = timezone(timedelta(hours=-3))
        date_time_now = datetime.now(tz=time_zone).isoformat()

        user = baker.make(
            User,
            cpf=gen.cpf(),
            date_joined=date_time_now,
            last_login=date_time_now,
            avatar=None,
        )
        serializer = UserDetailSerializer(user)

        expected_data = {
            "id": str(user.id),
            "email": user.email,
            "name": user.name,
            "cpf": user.cpf,
            "address": user.address,
            "is_active": user.is_active,
            "date_joined": user.date_joined if user.date_joined else None,
            "last_login": user.last_login if user.last_login else None,
            "avatar": user.avatar if user.avatar else None,
        }

        assert serializer.data == expected_data

    def test_list_serializer_with_no_user(self) -> None:
        user = {}
        serializer = UserDetailSerializer(user)
        assert serializer.data == {"avatar": None}
