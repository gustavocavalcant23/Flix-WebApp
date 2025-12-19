import csv
from django.core.management.base import BaseCommand
from django.db import transaction

from genres.models import Genre


class Command(BaseCommand):
    help = "Import genres from CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "file_name",
            type=str,
            help="CSV file path"
        )

    @transaction.atomic
    def handle(self, *args, **options):
        file_name = options["file_name"]

        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            counter = 0

            for row in reader:
                name = row["name"].strip()

                genre, created = Genre.objects.get_or_create(
                    name=name
                )

                if created:
                    counter += 1
                    self.stdout.write(
                        self.style.WARNING(
                            f"THE GENRE {name.upper()} WAS IMPORTED!"
                        )
                    )

        self.stdout.write(
            self.style.SUCCESS(
                f"DONE! {counter} GENRES IMPORTED SUCCESSFULLY!"
            )
        )
