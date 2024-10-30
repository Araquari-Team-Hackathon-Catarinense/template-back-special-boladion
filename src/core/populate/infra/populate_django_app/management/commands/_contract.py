from core.order.infra.order_django_app.models import Contract
from core.populate.infra.resources.data_contracts import generate_contract_data


def populate_contracts() -> None:
    if Contract.objects.exists():
        return
    print("Creating contracts...")

    contracts_to_create = [Contract(**data) for data in generate_contract_data()]
    print(contracts_to_create)

    Contract.objects.bulk_create(contracts_to_create)
