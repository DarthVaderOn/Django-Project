from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.likes import LikePostSerializer, LikeCommentSerializer
from likes_app.models import LikePost, LikeComment


class LikePostsView(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    serializer_class = LikePostSerializer
    queryset = LikePost.objects.filter()
    filter_backends = [filters.OrderingFilter]


class LikeCommentsView(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.filter()
    filter_backends = [filters.OrderingFilter]