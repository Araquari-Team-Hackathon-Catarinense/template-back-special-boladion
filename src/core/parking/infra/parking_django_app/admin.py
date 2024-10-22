from django.contrib import admin

from .models import Operation, Parking, ParkingSector

admin.site.register(Parking)
admin.site.register(ParkingSector)
admin.site.register(Operation)
