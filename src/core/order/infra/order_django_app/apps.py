from django.apps import AppConfig


class ProductDjangoAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.order.infra.order_django_app"

    def ready(self):
        import core.order.infra.order_django_app.signals
