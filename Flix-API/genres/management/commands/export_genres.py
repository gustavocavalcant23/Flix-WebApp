import csv
from django.core.management.base import BaseCommand
from django.db import transaction

from genres.models import Genre


class Command(BaseCommand):
    help = "Export genres to CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "--output",
            type=str,
            default="exported_genres.csv",
            help="Output CSV file name"
        )

    @transaction.atomic
    def handle(self, *args, **options):
        output_file = options["output"]
        genres = Genre.objects.all()

        try:
            with open(output_file, mode="w", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["id", "name"]
                )

                writer.writeheader()
                counter = 0

                for genre in genres:
                    writer.writerow({
                        "id": genre.id,
                        "name": genre.name
                    })
                    counter += 1

        except OSError as e:
            self.stderr.write(
                self.style.ERROR(
                    f"ERROR WHILE EXPORTING GENRES: {e}"
                )
            )
            return

        self.stdout.write(
            self.style.SUCCESS(
                f"DONE! {counter} GENRES EXPORTED SUCCESSFULLY!"
            )
        )
