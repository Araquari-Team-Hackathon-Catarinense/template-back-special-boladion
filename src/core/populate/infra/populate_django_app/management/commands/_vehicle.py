from core.populate.infra.resources.data_vehicle import bodies_data, modalities_data
from core.vehicle.infra.vehicle_django_app.models import Body, Modality


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
