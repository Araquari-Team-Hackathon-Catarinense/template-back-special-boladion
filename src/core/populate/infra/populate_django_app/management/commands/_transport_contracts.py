import traceback

from core.order.infra.order_django_app.models import TransportContract
from core.populate.infra.resources.data_transport_contracts import generate_transports


def populate_transports() -> None:
    if TransportContract.objects.exists():
        return

    transports_to_create = [TransportContract(**data) for data in generate_transports()]

    try:
        TransportContract.objects.bulk_create(transports_to_create)
    except Exception as e:
        print(f"Error creating TransportContract: {e}")
        traceback.print_exc()
        return
