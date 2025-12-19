from django.urls import path

from .views import GenreCreateListView, GenreRetriveUpdateDestroyView


urlpatterns = [

    path('genres/', GenreCreateListView.as_view(), name='genre_list'),
    path('genres/<int:pk>/', GenreRetriveUpdateDestroyView.as_view(), name='genre_rud'),

]
