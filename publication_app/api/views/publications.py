from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.publications import PostSerializer
from publication_app.models import Post


# CRUD
class PostsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter]
    ordering_field = ['created_at', 'id']


    def perform_destroy(self, instance):
        instance.is_public = False
        instance.save()