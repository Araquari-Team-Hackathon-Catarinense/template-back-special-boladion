import uuid
from django.db import models

from core.company.domain.value_objects import PersonType


class Company(models.Model):

    PERSON_TYPE_CHOICES = [
        (person_type.name, person_type.value) for person_type in PersonType
    ]

    id = models.UUIDField(primary_key=True, editable=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    trade_name = models.CharField(max_length=255, blank=True, null=True)
    person_type = models.CharField(max_length=2, choices=PERSON_TYPE_CHOICES)
    document_number = models.CharField(max_length=14, unique=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    system_admin = models.BooleanField(default=False, blank=True, null=True)
    address = models.JSONField(blank=True, null=True)
    contacts = models.JSONField(blank=True, null=True)

    class Meta:
        db_table: str = "company"
        verbose_name_plural: str = "companies"

    def __str__(self) -> str:
        return f"{self.name} ({self.document_number})"
