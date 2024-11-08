from core.populate.infra.resources.data_user import drivers_data, users_data
from core.user.infra.user_django_app.models import Driver, User


def populate_users() -> None:
    if User.objects.exists():
        return

    users_to_create: list[User] = [User(**data) for data in users_data]
    User.objects.bulk_create(users_to_create)
    for user in users_to_create:
        user.set_password(user.password)
        user.save()


def populate_drivers() -> None:
    if Driver.objects.exists():
        return
    if User.objects.exists():
        drivers_to_create: list[Driver] = [Driver(**data) for data in drivers_data]
        Driver.objects.bulk_create(drivers_to_create)
