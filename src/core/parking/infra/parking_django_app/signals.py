from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.parking.infra.parking_django_app.admin import ParkingSector


@receiver(post_save, sender=ParkingSector)
def update_parking_slots(sender, instance, **kwargs):
    parking = instance.parking
    total_slots = parking.slots + instance.qty_slots
    parking.slots = total_slots
    parking.save()
