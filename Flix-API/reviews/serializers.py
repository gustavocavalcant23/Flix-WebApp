from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    movie_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id',
            'movie_name',
            'stars',
        ]

    def get_movie_name(self, obj):
        movie_name = obj.movie.name
        if movie_name:
            return movie_name
        return None
