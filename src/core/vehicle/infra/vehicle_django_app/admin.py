from django.contrib import admin

from core.vehicle.infra.vehicle_django_app.models import Body, Modality, Vehicle

admin.site.register(Body)
admin.site.register(Modality)
admin.site.register(Vehicle)
