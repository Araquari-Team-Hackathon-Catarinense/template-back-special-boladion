# pylint: disable=no-member
from django.core.management.base import BaseCommand, CommandError, CommandParser

from core.populate.infra.populate_django_app.management.commands._company import (
    populate_companies,
)
from core.populate.infra.populate_django_app.management.commands._measurement_unit import (
    populate_measurement_units,
)

from ._company import populate_companies
from ._user import populate_users


class Command(BaseCommand):
    help = "Populate the database with the initial data"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--companies",
            action="store_true",
            help="Populate the companies data",
        )
        parser.add_argument(
            "--users",
            action="store_true",
            help="Populate the users data",
        )
        parser.add_argument(
            "--measurement_units",
            action="store_true",
            help="Populate the measurement units data",
        )
        parser.add_argument(
            "--all", action="store_true", help="Populate all data available"
        )

    def handle(self, *args, **options):
        try:
            if options.get("all"):
                self.__handle_all()
            if options.get("companies"):
                self.__handle_companies()
            if options.get("users"):
                self.__handle_users()
            if options.get("measurement_units"):
                self.__handle_measurement_units()

            self.stdout.write(self.style.SUCCESS("\nTudo populado com sucesso! :D"))
        except CommandError as exc:
            raise CommandError(f"An error occurred: {exc}") from exc
        except Exception as e:
            raise CommandError(f"An error occurred: {e}") from e

    def __handle_companies(self):
        self.stdout.write("Populating companies data...", ending="")
        populate_companies()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_users(self):
        self.stdout.write("Populating users data...", ending="")
        populate_users()

    def __handle_measurement_units(self):
        self.stdout.write("Populating measurement units data...", ending="")
        populate_measurement_units()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_all(self):
        self.stdout.write("Populating all data...", ending="")
        self.__handle_companies()
        self.__handle_users()
        populate_companies()
        populate_measurement_units()
        self.stdout.write(self.style.SUCCESS("OK"))
