from django.db import models
from django.db.models import Q, Sum
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from core.__seedwork__.infra.django_app.models import BaseModel
from core.company.infra.company_django_app.models import Company
from core.order.domain.value_objects import OperationType
from core.product.infra.product_django_app.models import Product
from core.user.infra.user_django_app.models import Driver
from core.vehicle.infra.vehicle_django_app.models import Composition


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

    def __str__(self) -> str:
        return f"{self.purchase_sale_order.company.name} - {self.purchase_sale_order.client.name}, {self.quantity}, {self.balance}"


class Trip(BaseModel):
    transport_contract = models.ForeignKey(
        TransportContract, on_delete=models.PROTECT, null=True, related_name="trips"
    )
    quantity = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    order_number = models.CharField(max_length=45, blank=True, null=True)
    vehicle = models.ForeignKey(
        Composition, on_delete=models.PROTECT, null=True, related_name="vehicle_trips"
    )
    driver = models.ForeignKey(
        Driver, on_delete=models.PROTECT, null=True, related_name="driver_trips"
    )

    def __str__(self) -> str:
        return f"{self.transport_contract.purchase_sale_order.company.name} - {self.transport_contract.purchase_sale_order.client.name}, {self.quantity}"


@receiver(pre_save, sender=Trip)
def balance(instance, **kwargs) -> None:  # pylint: disable=unused-argument
    if instance.deleted_at is None:
        transport_contract = instance.transport_contract
        if instance.quantity <= 0 or instance.quantity is None:
            raise ValueError("A quantidade não pode ser menor ou igual a zero.")
        else:
            if (
                instance.quantity > transport_contract.balance
                and instance._state.adding
            ):  # pylint: disable=protected-access
                raise ValueError(
                    "A quantidade não pode ser maior que o saldo restante."
                )
            elif instance._state.adding is False:  # pylint: disable=protected-access
                old_trip = Trip.objects.get(id=instance.id)
                a = transport_contract.balance + old_trip.quantity
                if instance.quantity > a:
                    raise ValueError(
                        "A quantidade não pode ser maior que o saldo restante."
                    )

            filtered_trips = transport_contract.trips.filter(~Q(id=instance.id))

            if filtered_trips.count() == 0:
                transport_contract.balance = (
                    transport_contract.quantity - instance.quantity
                )
            else:
                print("estou aqui amigo")
                transport_contract.balance = (
                    transport_contract.quantity
                    - instance.quantity
                    - filtered_trips.aggregate(Sum("quantity"))["quantity__sum"]
                )

            transport_contract.save()


@receiver(post_save, sender=Trip)
def balance_delete(instance, **kwargs) -> None:  # pylint: disable=unused-argument
    if instance.deleted_at is not None:
        transport_contract = instance.transport_contract
        if transport_contract.trips.count() == 0:
            transport_contract.balance = transport_contract.quantity
            transport_contract.save()
        else:
            transport_contract.balance = (
                transport_contract.quantity
                - transport_contract.trips.aggregate(Sum("quantity"))["quantity__sum"]
            )
            transport_contract.save()
