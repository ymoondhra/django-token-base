from rest_framework import generics

from . import models
from .serializers import UserSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = UserSerializer
