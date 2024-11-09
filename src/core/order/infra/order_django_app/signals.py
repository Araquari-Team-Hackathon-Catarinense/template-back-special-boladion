from django.db.models.signals import post_save
from django.dispatch import receiver

from core.order.infra.order_django_app.models import PurchaseSaleOrder


@receiver(post_save, sender=PurchaseSaleOrder)
def balance(sender, instance, created, **kwargs):
    if created:
        instance.balance = instance.quantity
        instance.save()
