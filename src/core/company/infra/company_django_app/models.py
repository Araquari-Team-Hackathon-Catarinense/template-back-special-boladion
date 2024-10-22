import uuid

from django.db import models

from core.company.domain.value_objects import PersonType
from core.image.infra.image_django_app.models import ImageProfilePic
from core.user.infra.user_django_app.models import User


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
    pic = models.ForeignKey(
        ImageProfilePic, on_delete=models.PROTECT, default="", blank=True, null=True
    )

    class Meta:
        db_table: str = "company"
        verbose_name_plural: str = "companies"

    def __str__(self) -> str:
        return f"{self.name} ({self.document_number})"


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, editable=True, default=uuid.uuid4)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employees")
    is_active = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        db_table: str = "employee"
        verbose_name_plural: str = "employees"

    def __str__(self) -> str:
        return f"{self.user} ({self.company})"
