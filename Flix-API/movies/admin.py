from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'genre')
    list_filter = ('genre', )
    search_fields = ('name', 'genre')
