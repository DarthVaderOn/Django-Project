from rest_framework import permissions
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.likes import LikePostSerializer, LikeCommentSerializer
from likes_app.models import LikePost, LikeComment


class LikePostsViewSet(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    """Создаём класс вьюсет лайков постов"""
    serializer_class = LikePostSerializer
    permission_classes = [permissions.IsAuthenticated]                       # просмотр лайков постов только для авторизованного пользователя
    queryset = LikePost.objects.all()


class LikeCommentsViewSet(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    """Создаём класс вьюсет лайков комментариев"""
    serializer_class = LikeCommentSerializer
    permission_classes = [permissions.IsAuthenticated]                       # просмотр лайков комментариев только для авторизованного пользователя
    queryset = LikeComment.objects.all()