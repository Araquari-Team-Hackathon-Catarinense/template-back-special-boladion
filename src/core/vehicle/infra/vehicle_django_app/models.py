import uuid

from celery.app import base
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


class Composition(BaseModel):
    axle = models.IntegerField()
    gross_weight = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "composition"
        verbose_name_plural = "compositions"

    def __str__(self) -> str:
        return f"{self.axle}, {self.gross_weight}, {self.date}, {self.is_active}"


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
    documents = models.ManyToManyField(Document, related_name="+")

    class Meta:
        db_table = "vehicle"
        verbose_name_plural = "vehicles"

    def __str__(self) -> str:
        return f"{self.license}, {self.chassis}, {self.renavam}, {self.vehicle_type}"


class VehicleComposition(models.Model):
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE, related_name="vehicle"
    )
    composition = models.ForeignKey(
        Composition, on_delete=models.CASCADE, related_name="composition"
    )
    sequence = models.IntegerField()

    class Meta:
        db_table = "vehicle_composition"
        verbose_name_plural = "vehicles_compositions"

    def __str__(self) -> str:
        return f"{self.vehicle}, {self.composition}"
