# pylint: disable=no-member
from django.core.management.base import BaseCommand, CommandError, CommandParser

from core.populate.infra.populate_django_app.management.commands import (
    populate_bodies,
    populate_companies,
    populate_measurement_units,
    populate_modalities,
    populate_packings,
    populate_users,
)
from core.populate.infra.populate_django_app.management.commands._product import (
    populate_products,
)


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
            "--packing",
            action="store_true",
            help="Populate the packing data",
        )
        parser.add_argument(
            "--products",
            action="store_true",
            help="Populate the products data",
        )
        parser.add_argument(
            "--vehicles",
            action="store_true",
            help="Populate the vehicles data",
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
            if options.get("packing"):
                self.__handle_packing()
            if options.get("products"):
                self.__handle_products()
            if options.get("vehicles"):
                self.__handle_vehicles()
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
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_measurement_units(self):
        self.stdout.write("Populating measurement units data...", ending="")
        populate_measurement_units()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_packing(self):
        self.stdout.write("Populating packing data...", ending="")
        populate_packings()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_products(self):
        self.stdout.write("Populating products data...", ending="")
        populate_products()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_vehicles(self):
        self.stdout.write("Populating vehicles data...", ending="")
        populate_bodies()
        populate_modalities()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_all(self):
        self.stdout.write("Populating all data...", ending="")
        self.__handle_companies()
        self.__handle_users()
        self.__handle_measurement_units()
        self.__handle_packing()
        self.__handle_products()
        self.__handle_vehicles()
        self.stdout.write(self.style.SUCCESS("OK"))
