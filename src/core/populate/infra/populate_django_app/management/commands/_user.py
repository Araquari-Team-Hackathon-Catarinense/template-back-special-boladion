from core.user.infra.user_django_app.models import User
from core.populate.infra.resources.data_user import users_data


def populate_users() -> None:
    if User.objects.exists():
        # for user_data in users_data:
        #     user = User.objects.filter(email=user_data["email"]).first()
        #     if user:
        #         user.set_password(user_data["password"])
        #         user.save()
        return

    users_to_create: list[User] = [User(**data) for data in users_data]
    User.objects.bulk_create(users_to_create)
