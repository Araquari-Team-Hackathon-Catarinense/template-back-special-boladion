from core.populate.infra.resources.data_measurement_unit import (
    generate_measurement_units,
)
from core.product.infra.product_django_app.models import MeasurementUnit


def populate_measurement_units() -> None:
    if MeasurementUnit.objects.exists():
        return

    measurement_units_to_create = [
        MeasurementUnit(**measurement_unit)
        for measurement_unit in generate_measurement_units()
    ]

    MeasurementUnit.objects.bulk_create(measurement_units_to_create)
