from rest_framework import filters
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.tags import TagSerializer
from tags_app.models import Tag


class TagViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """Создаём класс вьюсет тегов"""
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'