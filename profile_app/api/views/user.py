from django.contrib.auth.models import User
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from profile_app.api.serializers.user import UserSerializer
from rest_framework import filters


class UserView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """Создаём класс вьюсет профиля"""
    serializer_class = UserSerializer
    queryset = User.objects.filter()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['username',]