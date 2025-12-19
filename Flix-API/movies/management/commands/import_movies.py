import csv
from django.core.management.base import BaseCommand
from django.db import transaction

from movies.models import Movie
from genres.models import Genre
from actors.models import Actor


class Command(BaseCommand):
    help = "Import movies from CSV"

    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    @transaction.atomic
    def handle(self, *args, **options):
        file_name = options["file_name"]
        counter = 0

        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    genre_id = int(row["genre"])
                    genre = Genre.objects.get(id=genre_id)

                    movie = Movie.objects.create(
                        name=row["name"],
                        release_date=int(row["release_date"]),
                        genre=genre,
                    )

                    actor_ids = [
                        int(a)
                        for a in row["actors"].split("|")
                        if a.strip().isdigit()
                    ]

                    valid_actors = Actor.objects.filter(id__in=actor_ids)

                    movie.actors.set(valid_actors)

                    counter += 1
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"MOVIE '{movie.name}' CREATED"
                        )
                    )

                except Genre.DoesNotExist:
                    self.stderr.write(
                        self.style.ERROR(
                            f"GENRE ID {row['genre']} NOT FOUND — MOVIE SKIPPED"
                        )
                    )

                except Exception as e:
                    self.stderr.write(
                        self.style.ERROR(
                            f"ERROR ON MOVIE '{row.get('name')}': {e}"
                        )
                    )

        self.stdout.write(
            self.style.SUCCESS(
                f"DONE! {counter} MOVIES IMPORTED SUCCESSFULLY!"
            )
        )
