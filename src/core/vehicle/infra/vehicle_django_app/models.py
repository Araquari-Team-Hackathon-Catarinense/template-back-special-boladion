import uuid

from django.db import models


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
