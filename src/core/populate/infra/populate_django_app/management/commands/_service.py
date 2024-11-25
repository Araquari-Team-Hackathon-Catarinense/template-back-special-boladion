from core.populate.infra.resources.data_service import generate_services
from core.service.infra.service_django_app.models import Service


def populate_services() -> None:
    if Service.objects.exists():
        return

    services_to_create: list[Service] = [
        Service(**data) for data in generate_services()
    ]
    Service.objects.bulk_create(services_to_create)
