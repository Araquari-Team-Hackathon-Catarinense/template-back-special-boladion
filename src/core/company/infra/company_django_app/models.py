import uuid

from django.db import models

from core.__seedwork__.infra.django_app.models import BaseModel
from core.company.domain.value_objects import ContractType, PersonType
from core.uploader.infra.uploader_django_app.models import Document
from core.user.infra.user_django_app.models import User


class Company(BaseModel):

    PERSON_TYPE_CHOICES = [
        (person_type.name, person_type.value) for person_type in PersonType
    ]

    name = models.CharField(max_length=255)
    trade_name = models.CharField(max_length=255, blank=True, null=True)
    person_type = models.CharField(max_length=2, choices=PERSON_TYPE_CHOICES)
    document_number = models.CharField(max_length=14, unique=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    system_admin = models.BooleanField(default=False, blank=True, null=True)
    address = models.JSONField(blank=True, null=True)
    contacts = models.JSONField(blank=True, null=True)
    documents = models.ManyToManyField(
        Document, related_name="company_document", blank=True
    )
    avatar = models.ForeignKey(
        Document,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    class Meta:
        db_table: str = "company"
        verbose_name_plural: str = "companies"

    def __str__(self) -> str:
        return f"{self.name} ({self.document_number})"


class Employee(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employees")
    is_active = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        db_table: str = "employee"
        verbose_name_plural: str = "employees"

    def __str__(self) -> str:
        return f"{self.user} ({self.company})"


class Contract(BaseModel):
    CONTRACT_TYPE_CHOICES = [
        (contract_type.name, contract_type.value) for contract_type in ContractType
    ]

    source_company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="source_contracts"
    )
    target_company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="target_contracts"
    )
    contract_type = models.CharField(max_length=255, choices=CONTRACT_TYPE_CHOICES)

    class Meta:
        db_table: str = "contract"
        verbose_name_plural: str = "contracts"

    def __str__(self) -> str:
        return f"{self.source_company.name} - {self.target_company.name} ({self.contract_type})"
