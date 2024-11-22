from django.db import models

from core.__seedwork__.infra.django_app.models import BaseModel
from core.parking.infra.parking_django_app.models import Parking


class Service(BaseModel):
    description = models.CharField(max_length=70)
    payment_rules = models.JSONField()
    parking = models.ForeignKey(
        Parking, on_delete=models.PROTECT, related_name="services"
    )

    class Meta:
        db_table: str = "service"
        verbose_name_plural: str = "services"
