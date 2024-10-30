# pylint: disable=no-member
from django.core.management.base import BaseCommand, CommandError, CommandParser

from core.populate.infra.populate_django_app.management.commands import (
    populate_companies,
    populate_contracts,
    populate_measurement_units,
    populate_packings,
    populate_products,
    populate_purchase_sale_orders,
    populate_users,
)
from core.populate.infra.populate_django_app.management.commands._vehicle import (
    populate_bodies,
    populate_modalities,
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
            "--contracts",
            action="store_true",
            help="Populate the contracts data",
        )
        parser.add_argument(
            "--purchase",
            action="store_true",
            help="Populate the purchase data",
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
            if options.get("contracts"):
                self.__handle_contracts()
            if options.get("purchase_sale_orders"):
                self.__handle_purchase_sale_orders()

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

    def __handle_contracts(self):
        self.stdout.write("Populating contracts data...", ending="")
        populate_contracts()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_purchase_sale_orders(self):
        self.stdout.write("Populating purchase sale orders data...", ending="")
        populate_purchase_sale_orders()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_all(self):
        self.stdout.write("Populating all data...", ending="")
        self.__handle_companies()
        self.__handle_users()
        self.__handle_measurement_units()
        self.__handle_packing()
        self.__handle_products()
        self.__handle_vehicles()
        self.__handle_contracts()
        self.__handle_purchase_sale_orders()
        self.stdout.write(self.style.SUCCESS("OK"))
