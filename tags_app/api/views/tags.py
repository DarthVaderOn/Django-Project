from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.tags import TagSerializer
from tags_app.models import Tag


# CRUD
class TagView(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    serializer_class = TagSerializer
    queryset = Tag.objects.filter()
    filter_backends = [filters.OrderingFilter]


    def perform_destroy(self, instance):
        instance.title = False
        instance.save()