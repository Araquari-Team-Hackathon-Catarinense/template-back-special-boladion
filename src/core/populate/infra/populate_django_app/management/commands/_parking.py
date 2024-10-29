from core.company.infra.company_django_app.models import Company
from core.parking.infra.parking_django_app.models import (
    Operation,
    Parking,
    ParkingSector,
)
from core.populate.infra.resources.data_parking import (
    operations_data,
    parking_sectors_data,
    parkings_data,
)


def populate_parkings() -> None:
    if Parking.objects.exists():
        return

    for company in Company.objects.all():
        parkings_to_create = [
            Parking(company=company, **data) for data in parkings_data
        ]
        Parking.objects.bulk_create(parkings_to_create)


def populate_parking_sectors() -> None:
    if ParkingSector.objects.exists():
        return

    for parking in Parking.objects.all():
        sectors_to_create = [
            ParkingSector(parking=parking, **data) for data in parking_sectors_data
        ]
        ParkingSector.objects.bulk_create(sectors_to_create)
        for sector in sectors_to_create:
            sector.save()


def populate_operations() -> None:
    if Operation.objects.exists():
        return

    for parking in Parking.objects.all():
        operations_to_create = [
            Operation(parking=parking, **data) for data in operations_data
        ]
        Operation.objects.bulk_create(operations_to_create)
