from django.contrib import admin

from .models import MeasurementUnit, Packing, PurchaseSaleOrder

admin.site.register(MeasurementUnit)
admin.site.register(Packing)
admin.site.register(PurchaseSaleOrder)
