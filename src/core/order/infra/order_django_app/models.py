from django.db import models

from core.__seedwork__.infra.django_app.models import BaseModel
from core.company.infra.company_django_app.models import Company
from core.order.domain.value_objects import OperationType
from core.product.infra.product_django_app.models import Product


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


class PurchaseSaleOrder(BaseModel):
    OPERATION_TYPE_CHOICES = [
        (operation_type.name, operation_type.value) for operation_type in OperationType
    ]

    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    client = models.ForeignKey(
        Company, on_delete=models.PROTECT, related_name="client_orders"
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    measurement_unit = models.ForeignKey(
        MeasurementUnit,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="measurement_unit_orders",
    )
    packing = models.ForeignKey(
        Packing,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="packing_orders",
    )
    operation_terminal = models.ForeignKey(
        Company, on_delete=models.PROTECT, related_name="operation_terminal_orders"
    )
    quantity = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    operation_type = models.CharField(max_length=255, choices=OPERATION_TYPE_CHOICES)

    class Meta:
        db_table: str = "purchase_sale_order"
        verbose_name_plural: str = "purchase_sale_orders"

    # def validate_source_client(self):
    #     # Verifica se existe um contrato do tipo CLIENTE onde a company é a source_company
    #     if not Contract.objects.filter(
    #         source_company=self.company,
    #         target_company=self.client,
    #         contract_type=ContractType.CLIENTE.value,
    #     ).exists():
    #         raise ValidationError(
    #             "O cliente deve ser uma empresa com um contrato do tipo CLIENTE com a empresa fornecedora."
    #         )

    def __str__(self):
        return f"{self.company.name} - {self.client.name}"


class TransportContract(BaseModel):
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, related_name="transport_contracts"
    )
    carrier = models.ForeignKey(
        Company, on_delete=models.PROTECT, related_name="carrier_contracts"
    )
    purchase_sale_order = models.ForeignKey(PurchaseSaleOrder, on_delete=models.PROTECT)
    quantity = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
