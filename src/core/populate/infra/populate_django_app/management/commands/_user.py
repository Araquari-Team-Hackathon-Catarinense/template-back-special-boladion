from core.populate.infra.resources.data_user import users_data
from core.user.infra.user_django_app.models import User


def populate_users() -> None:
    if User.objects.exists():
        return

    users_to_create: list[User] = [User(**data) for data in users_data]
    User.objects.bulk_create(users_to_create)
    for user in users_to_create:
        user.set_password(user.password)
        user.save()
