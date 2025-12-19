from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.SmallIntegerField(
        default=0,
        validators=[
            MinValueValidator(0, 'O valor mínimo é 0.'),
            MaxValueValidator(5, 'O valor máximo é 5.')
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.movie}, rated as {self.stars} stars.'
