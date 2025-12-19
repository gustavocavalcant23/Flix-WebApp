from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'stars')
    list_filter = ('stars', )
    search_fields = ('movie', )
