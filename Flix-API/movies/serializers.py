from rest_framework import serializers
from django.db.models import Avg

from .models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorsSerializer


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value < 1900:
            raise serializers.ValidationError(
                'The release date cannot be before than 1900.'
            )
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    reviews_numbers = serializers.SerializerMethodField(read_only=True)
    genre = GenreSerializer()
    actors = ActorsSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            'id',
            'name',
            'genre',
            'actors',
            'release_date',
            'rate',
            'reviews_numbers',
            'synopsis',
        ]

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 2)

        return None

    def get_reviews_numbers(self, obj):
        reviews = obj.reviews.count()
        if reviews:
            return reviews
        return None
