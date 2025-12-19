from django.urls import path

from .views import MovieCreateListView, MovieRetrieveUpdateDestroyView, MovieStatsView


urlpatterns = [

    path('movies/', MovieCreateListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie_rud'),
    path('movies/stats/', MovieStatsView.as_view(), name='movie_stats'),

]
