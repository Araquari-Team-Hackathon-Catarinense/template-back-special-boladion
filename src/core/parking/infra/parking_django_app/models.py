import uuid

from django.db import models

from core.__seedwork__.infra.django_app.models import BaseModel
from core.company.infra.company_django_app.models import Company, Contract
from core.parking.domain.value_objects import SectorType


class Parking(BaseModel):
    description = models.CharField(max_length=45)
    slots = models.IntegerField(default=0)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="parking"
    )

    class Meta:
        db_table: str = "parking"
        verbose_name_plural: str = "parkings"


class ParkingSector(BaseModel):
    SECTOR_TYPE_CHOICES = [
        (sector_type.name, sector_type.value) for sector_type in SectorType
    ]
    description = models.CharField(max_length=45)
    qty_slots = models.IntegerField(default=0)
    sector_type = models.CharField(max_length=8, choices=SECTOR_TYPE_CHOICES)
    parking = models.ForeignKey(
        Parking, on_delete=models.CASCADE, related_name="sectors"
    )
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, related_name="sectors", null=True
    )

    class Meta:
        db_table: str = "parking_sector"
        verbose_name_plural: str = "parking_sectors"


class Operation(BaseModel):
    name = models.CharField(max_length=45)
    parking = models.ForeignKey(
        Parking, on_delete=models.CASCADE, related_name="operations"
    )

    class Meta:
        db_table: str = "operation"
        verbose_name_plural: str = "operations"
