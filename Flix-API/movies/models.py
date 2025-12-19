from django.db import models

from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    name = models.CharField('Filme', max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
    release_date = models.PositiveIntegerField('Ano de Lançamento', null=True, blank=True)
    synopsis = models.TextField('Sinopse', max_length=500, null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies')

    def __str__(self):
        return f'{self.name}, {self.release_date}'
