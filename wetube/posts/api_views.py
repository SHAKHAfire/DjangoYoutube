from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAdminUser

from .models import Posts
from .serializers import PostSerializer


class PostViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    permission_classes = [IsAdminUser]
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
