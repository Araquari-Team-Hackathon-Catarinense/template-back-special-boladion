import uuid

from django.db import models
from core.__seedwork__.infra.django_app.models import BaseModel

import vehicle


class Body(models.Model):
    id = models.UUIDField(primary_key=True, editable=True, default=uuid.uuid4)
    description = models.CharField(max_length=45)

    class Meta:
        db_table = "body"
        verbose_name_plural = "bodies"


class Modality(models.Model):
    id = models.UUIDField(primary_key=True, editable=True, default=uuid.uuid4)
    description = models.CharField(max_length=45)
    axle = models.IntegerField()

    class Meta:
        db_table = "modality"
        verbose_name_plural = "modalities"


class Vehicle(BaseModel):
    license = models.CharField(max_length=10)
    chassis = models.CharField(max_length=45)
    renavam = models.CharField(max_length=45)
    axle = models.IntegerField()
    year = models.IntegerField()
    gross_weight = integerField()
    vehicle
