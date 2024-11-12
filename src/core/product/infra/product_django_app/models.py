from django.db import models

from core.__seedwork__.infra.django_app.models import BaseModel
from core.company.infra.company_django_app.models import Company


class Product(BaseModel):
    description = models.CharField(max_length=200)
    internal_code = models.CharField(max_length=45, unique=True)
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="products"
    )

    class Meta:
        db_table: str = "product"
        verbose_name_plural: str = "products"

    def __str__(self) -> str:
        return f"{self.description} ({self.company.name})"
