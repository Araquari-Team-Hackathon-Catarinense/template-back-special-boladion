from core.populate.infra.resources.data_vehicle import bodies_data
from core.vehicle.infra.vehicle_django_app.models import Body


def populate_bodies() -> None:
    if Body.objects.exists():
        return

    bodies_to_create = [Body(**body) for body in bodies_data]

    Body.objects.bulk_create(bodies_to_create)
