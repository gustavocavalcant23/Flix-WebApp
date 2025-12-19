from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.permissions import GlobalDefaultPermission
from .models import Actor
from .serializers import ActorsSerializer
# Create your views here.


class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorsSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorsSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
