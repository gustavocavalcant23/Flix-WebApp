from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated

from .models import Movie
from reviews.models import Review
from core.permissions import GlobalDefaultPermission
from .serializers import MovieSerializer, MovieListDetailSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer


class MovieStatsView(views.APIView):
    queryset = Movie.objects.all()
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)

    def get(self, request, *args, **kwargs):
        total_movies = self.queryset.count()

        movies_by_genre = self.queryset.values(
            'genre__name',
        ).annotate(
            count=Count('id')
        )

        total_reviews = Review.objects.count()

        average_stars = Review.objects.aggregate(
            avg_stars=Avg('stars')
        )['avg_stars']

        average_stars = round(average_stars, 2) if average_stars else 0

        return response.Response(
            data={
                'total_movies': total_movies,
                'movies_by_genre': movies_by_genre,
                'total_reviews': total_reviews,
                'average_stars': average_stars
            },
            status=status.HTTP_200_OK,
        )
