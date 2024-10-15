# from django.db.models import Sum
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# @receiver(post_save, sender=ParkingSector)
# def update_parking_slots(sender, instance, **kwargs):
#     parking = instance.parking
#     total_slots = parking.sectors_set.aggregate(slots=Sum('qty_slots'))['slots']
#     parking.slots = total_slots
#     parking.save()
