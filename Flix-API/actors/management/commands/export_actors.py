import csv
from django.core.management.base import BaseCommand
from django.db import transaction

from actors.models import Actor


class Command(BaseCommand):
    help = "Export actors to CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "--output",
            type=str,
            default="exported_actors.csv",
            help="Output CSV file name"
        )

    @transaction.atomic
    def handle(self, *args, **options):
        output_file = options["output"]
        actors = Actor.objects.all()

        try:
            with open(output_file, mode="w", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["id", "name", "nationality"]
                )

                writer.writeheader()
                counter = 0

                for actor in actors:
                    writer.writerow({
                        "id": actor.id,
                        "name": actor.name,
                        "nationality": actor.nationality
                    })
                    counter += 1

        except OSError as e:
            self.stderr.write(
                self.style.ERROR(
                    f"ERROR WHILE EXPORTING ACTORS: {e}"
                )
            )
            return

        self.stdout.write(
            self.style.SUCCESS(
                f"DONE! {counter} ACTORS EXPORTED SUCCESSFULLY!"
            )
        )
