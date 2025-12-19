from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.permissions import GlobalDefaultPermission
from .models import Review
from .serializers import ReviewSerializer, ReviewListSerializer


class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewListSerializer
        return ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
