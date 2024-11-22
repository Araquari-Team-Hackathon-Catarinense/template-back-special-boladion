import traceback

from core.order.infra.order_django_app.models import (
    Composition,
    MeasurementUnit,
    Packing,
    PurchaseSaleOrder,
    TransportContract,
    Trip,
)
from core.populate.infra.resources.data_order import (
    composition_data,
    generate_measurement_units,
    generate_packings,
    generate_purchase_sale_orders,
    generate_transports,
    generate_trips,
)


def populate_measurement_units() -> None:
    if MeasurementUnit.objects.exists():
        return

    measurement_units_to_create = [
        MeasurementUnit(**measurement_unit)
        for measurement_unit in generate_measurement_units()
    ]

    MeasurementUnit.objects.bulk_create(measurement_units_to_create)


def populate_packings() -> None:
    if Packing.objects.exists():
        return

    packings_to_create = [Packing(**packing) for packing in generate_packings()]

    Packing.objects.bulk_create(packings_to_create)


def populate_purchase_sale_orders() -> None:
    if PurchaseSaleOrder.objects.exists():
        return

    purchase_sale_orders_to_create = [
        PurchaseSaleOrder(**data) for data in generate_purchase_sale_orders()
    ]
    PurchaseSaleOrder.objects.bulk_create(purchase_sale_orders_to_create)


def populate_transports_contract() -> None:
    if TransportContract.objects.exists():
        return

    transports_to_create = [TransportContract(**data) for data in generate_transports()]

    try:
        TransportContract.objects.bulk_create(transports_to_create)
    except Exception as e:
        print(f"Error creating TransportContract: {e}")
        traceback.print_exc()
        return


def populate_compositions() -> None:
    if Composition.objects.exists():
        return

    for composition in composition_data:
        Composition.objects.create(**composition)


def populate_trip() -> None:
    if TransportContract.objects.exists():
        print("Creating Trip...")
        trips_to_create = [Trip(**data) for data in generate_trips()]
        try:
            Trip.objects.bulk_create(trips_to_create)
        except Exception as e:
            print(f"Error creating Trip: {e}")
            traceback.print_exc()
            return
    else:
        print("No TransportContract to create Trip")
        return


def populate_composition() -> None:
    if Composition.objects.exists():

        return
    pass
