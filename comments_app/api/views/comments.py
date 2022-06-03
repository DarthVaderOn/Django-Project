from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.comments import CommentSerializer
from comments_app.models import Comments


class CommentsView(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    serializer_class = CommentSerializer
    queryset = Comments.objects.filter()
    filter_backends = [filters.OrderingFilter]


    def perform_destroy(self, instance):
        instance.is_public = False
        instance.save()