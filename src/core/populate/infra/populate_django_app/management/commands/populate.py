# pylint: disable=no-member
from django.core.management.base import BaseCommand, CommandError, CommandParser

from core.populate.infra.populate_django_app.management.commands._company import (
    populate_companies,
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
            "--all", action="store_true", help="Populate all data available"
        )

    def handle(self, *args, **options):
        try:
            if options.get("all"):
                self.__handle_all()
            if options.get("companies"):
                self.__handle_companies()

            self.stdout.write(self.style.SUCCESS("\nTudo populado com sucesso! :D"))
        except CommandError as exc:
            raise CommandError(f"An error occurred: {exc}") from exc
        except Exception as e:
            raise CommandError(f"An error occurred: {e}") from e

    def __handle_companies(self):
        self.stdout.write("Populating companies data...", ending="")
        populate_companies()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_all(self):
        self.stdout.write("Populating all data...", ending="")
        populate_companies()
        self.stdout.write(self.style.SUCCESS("OK"))
