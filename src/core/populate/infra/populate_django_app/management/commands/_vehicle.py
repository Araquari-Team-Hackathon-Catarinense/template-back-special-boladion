from core.populate.infra.resources.data_vehicle import (
    bodies_data,
    modalities_data,
    vehicles_data,
)
from core.vehicle.infra.vehicle_django_app.models import Body, Modality, Vehicle


def populate_bodies() -> None:
    if Body.objects.exists():
        return

    bodies_to_create = [Body(**body) for body in bodies_data]

    Body.objects.bulk_create(bodies_to_create)


def populate_modalities() -> None:
    if Modality.objects.exists():
        return

    modalities_to_create = [Modality(**modality) for modality in modalities_data]

    Modality.objects.bulk_create(modalities_to_create)


def populate_vehicles() -> None:
    if Vehicle.objects.exists():
        return

    if not Body.objects.exists():
        populate_bodies()

    if not Modality.objects.exists():
        populate_modalities()

    body = Body.objects.first()
    modality = Modality.objects.first()

    for vehicle in vehicles_data:
        vehicle["body"] = body
        vehicle["modality"] = modality

    vehicles_to_create = [Vehicle(**vehicle) for vehicle in vehicles_data]

    Vehicle.objects.bulk_create(vehicles_to_create)
