# pylint: disable=no-member
from django.core.management.base import BaseCommand, CommandError, CommandParser

from core.populate.infra.populate_django_app.management.commands import (
    populate_bodies,
    populate_companies,
    populate_compositions,
    populate_contracts,
    populate_drivers,
    populate_employee,
    populate_measurement_units,
    populate_modalities,
    populate_operations,
    populate_packings,
    populate_parking_sectors,
    populate_parkings,
    populate_products,
    populate_purchase_sale_orders,
    populate_services,
    populate_transports_contract,
    populate_trip,
    populate_users,
    populate_vehicles,
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
            "--order",
            action="store_true",
            help="Populate the measurement units data",
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
            "--parkings",
            action="store_true",
            help="Populate the parkings data",
        )
        parser.add_argument(
            "--services",
            action="store_true",
            help="Populate the services data",
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
            if options.get("drivers"):
                self.__handle_drivers()
            if options.get("products"):
                self.__handle_products()
            if options.get("vehicles"):
                self.__handle_vehicles()
            if options.get("contracts"):
                self.__handle_contracts()
            if options.get("order"):
                self.__handle_orders()
            if options.get("parkings"):
                self.__handle_parkings()
            if options.get("employees"):
                self.__handle_employee()
            if options.get("services"):
                self.__handle_services()

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

    def __handle_employee(self):
        self.stdout.write("Populating employees data...", ending="")
        populate_employee()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_drivers(self):
        self.stdout.write("Populating drivers data...", ending="")
        populate_drivers()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_orders(self):
        self.stdout.write("Populating orders data...", ending="")
        populate_measurement_units()
        populate_packings()
        populate_purchase_sale_orders()
        populate_transports_contract()
        populate_compositions()
        populate_trip()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_products(self):
        self.stdout.write("Populating products data...", ending="")
        populate_products()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_vehicles(self):
        self.stdout.write("Populating vehicles data...", ending="")
        populate_bodies()
        populate_modalities()
        populate_vehicles()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_contracts(self):
        self.stdout.write("Populating contracts data...", ending="")
        populate_contracts()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_parkings(self):
        self.stdout.write("Populating parkings data...", ending="")
        populate_parkings()
        populate_parking_sectors()
        populate_operations()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_services(self):
        self.stdout.write("Populating services data...", ending="")
        populate_services()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_all(self):
        self.stdout.write("Populating all data...", ending="")
        self.__handle_companies()
        self.__handle_users()
        self.__handle_employee()
        self.__handle_drivers()
        self.__handle_products()
        self.__handle_vehicles()
        self.__handle_contracts()
        self.__handle_orders()
        self.__handle_parkings()
        self.__handle_services()
        self.stdout.write(self.style.SUCCESS("OK"))
