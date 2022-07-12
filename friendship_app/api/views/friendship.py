from rest_framework import permissions
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.friendship import FriendshipSerializer, FollowSerializer
from ...models import FriendshipRequest, FollowRequest


class FriendshipViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    """Создаём класс вьюсет дружбы"""
    serializer_class = FriendshipSerializer
    permission_classes = [permissions.IsAuthenticated]                       # просмотр друзей только для авторизованного пользователя
    queryset = FriendshipRequest.objects.all()


class FollowViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    """Создаём класс вьюсет подписки"""
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]                       # просмотр подписчиков только для авторизованного пользователя
    queryset = FollowRequest.objects.all()