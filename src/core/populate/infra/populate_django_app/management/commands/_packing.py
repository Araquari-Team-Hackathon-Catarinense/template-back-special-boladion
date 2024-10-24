from core.populate.infra.resources.data_packing import (
    generate_packings,
)
from core.order.infra.order_django_app.models import Packing


def populate_packings() -> None:
    if Packing.objects.exists():
        return

    packings_to_create = [
        Packing(**packing)
        for packing in generate_packings()
    ]

    Packing.objects.bulk_create(packings_to_create)
