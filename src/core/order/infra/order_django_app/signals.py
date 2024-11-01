from django.db.models.signals import post_save
from django.dispatch import receiver

from core.order.infra.order_django_app.models import (
    PurchaseSaleOrder,
    TransportContract,
)


@receiver(post_save, sender=PurchaseSaleOrder)
def balance(sender, instance, created, **kwargs):
    if not hasattr(instance, "_already_saved"):
        instance._already_saved = True
        instance.quantity = instance.balance
        instance.save()
