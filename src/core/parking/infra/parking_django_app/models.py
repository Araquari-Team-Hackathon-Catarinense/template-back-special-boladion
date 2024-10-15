import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.company.infra.company_django_app.models import Company


class Parking(models.Model):
    id = models.UUIDField(primary_key=True, editable=True, default=uuid.uuid4)
    description = models.CharField(max_length=45)
    slots = models.IntegerField(default=0)
    entity = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="parking"
    )
