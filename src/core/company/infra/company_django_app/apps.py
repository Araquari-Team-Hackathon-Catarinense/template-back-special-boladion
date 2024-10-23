from django.apps import AppConfig


class CompanyAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.company.infra.company_django_app"

    def ready(self):
        import core.company.infra.company_django_app.signals
