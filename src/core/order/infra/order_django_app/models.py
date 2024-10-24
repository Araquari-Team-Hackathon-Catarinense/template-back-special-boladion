from django.db import models

from core.__seedwork__.infra.django_app.models import BaseModel
from core.company.infra.company_django_app.models import Company


class MeasurementUnit(BaseModel):
    description = models.CharField(max_length=45)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    class Meta:
        db_table: str = "measurement_unit"
        verbose_name_plural: str = "measurement units"

    def __str__(self) -> str:
        return f"{self.description}"


class Packing(BaseModel):
    description = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    class Meta:
        db_table: str = "packing"
        verbose_name_plural: str = "packings"

    def __str__(self) -> str:
        return f"{self.description}"
