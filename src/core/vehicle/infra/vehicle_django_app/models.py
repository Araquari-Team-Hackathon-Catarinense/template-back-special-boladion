import uuid

from django.db import models

from core.__seedwork__.infra.django_app.models import BaseModel
from core.uploader.infra.uploader_django_app.models import Document
from core.vehicle.domain.value_objects import VehicleType


class Body(models.Model):
    id = models.UUIDField(primary_key=True, editable=True, default=uuid.uuid4)
    description = models.CharField(max_length=45)

    class Meta:
        db_table = "body"
        verbose_name_plural = "bodies"

    def __str__(self) -> str:
        return f"{self.description}"


class Modality(models.Model):
    id = models.UUIDField(primary_key=True, editable=True, default=uuid.uuid4)
    description = models.CharField(max_length=45)
    axle = models.IntegerField()

    class Meta:
        db_table = "modality"
        verbose_name_plural = "modalities"

    def __str__(self) -> str:
        return f"{self.description}, {self.axle}"


class Vehicle(BaseModel):
    VEHICLE_TYPE_CHOICES = [
        (vehicle_type.name, vehicle_type.value) for vehicle_type in VehicleType
    ]
    license = models.CharField(max_length=10, unique=True)
    chassis = models.CharField(max_length=45, blank=True, null=True, unique=True)
    renavam = models.CharField(max_length=45, blank=True, null=True)
    axle = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    gross_weight = models.IntegerField(blank=True, null=True)
    vehicle_type = models.CharField(
        max_length=45, choices=VEHICLE_TYPE_CHOICES, default=VehicleType.CARRO
    )
    body = models.ForeignKey(
        Body,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="body",
    )
    modality = models.ForeignKey(
        Modality,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="modality",
    )

    class Meta:
        db_table = "vehicle"
        verbose_name_plural = "vehicles"

    def __str__(self) -> str:
        return f"{self.license}, {self.chassis}, {self.renavam}, {self.vehicle_type}"


class VehicleDocument(BaseModel):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    document = models.ForeignKey(Document, on_delete=models.PROTECT)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "vehicle_document"
        verbose_name_plural = "vehicle_documents"
        unique_together = [["vehicle", "document"]]

    def __str__(self) -> str:
        return f"{self.vehicle}, {self.document}, {self.description}"
