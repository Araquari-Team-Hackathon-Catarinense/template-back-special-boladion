from django.db.models import Sum
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from core.parking.infra.parking_django_app.admin import ParkingSector


@receiver(post_save, sender=ParkingSector)
def update_parking_slots_on_save(sender, instance, **kwargs):
    parking = instance.parking
    parking_sectors = parking.sectors.all()
    total_slots = parking_sectors.aggregate(Sum("qty_slots"))["qty_slots__sum"]
    parking.slots = total_slots
    parking.save()


@receiver(post_delete, sender=ParkingSector)
def update_parking_slots_on_delete(sender, instance, **kwargs):
    print("signals")
    parking = instance.parking
    if parking.sectors.count() == 0:
        total_slots = 0
    else:
        parking_sectors = parking.sectors.all()
        total_slots = parking_sectors.aggregate(Sum("qty_slots"))["qty_slots__sum"]
    parking.slots = total_slots
    parking.save()
