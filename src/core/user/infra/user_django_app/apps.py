from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.user.infra.user_django_app"

    def ready(self):
        import core.user.infra.user_django_app.signals
