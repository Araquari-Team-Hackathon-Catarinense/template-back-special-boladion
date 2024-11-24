from django.db.models import Q, Sum
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from core.order.infra.order_django_app.models import Trip


@receiver(pre_save, sender=Trip)
def change_transport_balance_when_add_a_new_trip(
    instance, **kwargs
) -> None:  # pylint: disable=unused-argument
    if instance.deleted_at is None:
        transport_contract = instance.transport_contract
        if instance.quantity is None or instance.quantity <= 0:
            raise ValueError("A quantidade não pode ser menor ou igual a zero.")
        else:
            if transport_contract.balance is None:
                transport_contract.balance = 0.0
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
                transport_contract.balance = (
                    transport_contract.quantity
                    - instance.quantity
                    - filtered_trips.aggregate(Sum("quantity"))["quantity__sum"]
                )

            transport_contract.save()


@receiver(post_save, sender=Trip)
def change_transport_balance_when_delete_a_trip(
    instance, **kwargs
) -> None:  # pylint: disable=unused-argument
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
