from core.company.infra.company_django_app.models import Contract
from core.populate.infra.resources.data_contracts import generate_contract_data


def populate_contracts() -> None:
    if Contract.objects.exists():
        return

    contracts_to_create = [Contract(**data) for data in generate_contract_data()]

    Contract.objects.bulk_create(contracts_to_create)
