from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAdminUser

from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    permission_classes=[IsAdminUser]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer