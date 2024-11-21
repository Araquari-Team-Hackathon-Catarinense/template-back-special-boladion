from django.contrib import admin

from .models import MeasurementUnit, Packing, PurchaseSaleOrder, TransportContract, Trip

admin.site.register(MeasurementUnit)
admin.site.register(Packing)
admin.site.register(PurchaseSaleOrder)
admin.site.register(TransportContract)
admin.site.register(Trip)
