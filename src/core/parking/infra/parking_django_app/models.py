import uuid

from django.db import models

from core.company.infra.company_django_app.models import Company
from core.parking.domain.value_objects import SectorType


class Parking(models.Model):
    id = models.UUIDField(primary_key=True, editable=True, default=uuid.uuid4)
    description = models.CharField(max_length=45)
    slots = models.IntegerField(default=0)
    entity = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="parking"
    )

    class Meta:
        db_table: str = "parking"
        verbose_name_plural: str = "parking"

class ParkingSector(models.Model):
    SECTOR_TYPE_CHOICES = [
        (sector_type.name, sector_type.value) for sector_type in SectorType
    ]

    id = models.UUIDField(primary_key=True, editable=True, default=uuid.uuid4)
    description = models.CharField(max_length=45)
    qty_slots = models.IntegerField(default=0)
    sector_type = models.CharField(max_length=8, choices=SECTOR_TYPE_CHOICES)
    parking = models.ForeignKey(
        Parking, on_delete=models.CASCADE, related_name="sectors"
    )
    # contract = models.ForeignKey(
    #     Contract, on_delete=models.CASCADE, related_name="sectors"
    # )

    class Meta:
        db_table: str = "parking_sector"
        verbose_name_plural: str = "parking_sector"
