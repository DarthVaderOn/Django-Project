from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from profile_app.api.serializers.user import ProfileSerializer
from profile_app.models import Profile
from rest_framework import filters


class ProfileView(GenericViewSet, ListModelMixin):
    """Создаём класс вьюсет профиля"""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.filter()
    filter_backends = [filters.OrderingFilter]