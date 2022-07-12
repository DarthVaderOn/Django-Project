from django.contrib.auth.models import User
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from profile_app.api.serializers.user import UserSerializer
from rest_framework import filters, permissions


class UserView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """Создаём класс вьюсет профиля"""
    serializer_class = UserSerializer
    queryset = User.objects.filter()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]                       # просмотр пользователей только для авторизованного пользователя
    search_fields = ['username',]