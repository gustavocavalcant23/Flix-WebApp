from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.permissions import GlobalDefaultPermission
from .models import Genre
from .serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)


class GenreRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
