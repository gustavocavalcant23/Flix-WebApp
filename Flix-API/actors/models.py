from django.db import models


NACIONALITY_CHOICES = [
    ('USA', 'American'),
    ('BRL', 'Brazilian'),
    ('UK', 'British'),
]


class Actor(models.Model):
    name = models.CharField('Nome', max_length=255)
    nationality = models.CharField('Nacionalidade', max_length=50, choices=NACIONALITY_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name
