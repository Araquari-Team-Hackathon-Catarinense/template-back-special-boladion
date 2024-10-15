from django.apps import AppConfig


class ParkingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.parking.infra.parking_django_app"

    def ready(self):
        import core.parking.infra.parking_django_app.signals
