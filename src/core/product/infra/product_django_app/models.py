import uuid

from django.db import models

from core.company.infra.company_django_app.models import Company


class MeasurementUnit(models.Model):
    id = models.UUIDField(primary_key=True, editable=True, default=uuid.uuid4)
    description = models.CharField(max_length=45)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    class Meta:
        db_table: str = "measurement_unit"
        verbose_name_plural: str = "measurement units"

    def __str__(self) -> str:
        return f"{self.description}"


class Packing(models.Model):
    id = models.UUIDField(primary_key=True, editable=True, default=uuid.uuid4)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
