import random

from core.company.infra.company_django_app.models import Company, Employee
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


def populate_employee() -> None:
    if not Company.objects.exists():
        print("No companies found. Populate companies first.")
        return

    if not User.objects.exists():
        print("No users found. Populate users first.")
        return

    companies = list(Company.objects.all())
    users = list(User.objects.all())

    print("Creating employees...")
    employees_to_create = []

    for _ in range(35):
        company = random.choice(companies)
        user = random.choice(users)

        employee = Employee(company=company, user=user)
        employees_to_create.append(employee)

    Employee.objects.bulk_create(employees_to_create)
    print("Employees created successfully.")
