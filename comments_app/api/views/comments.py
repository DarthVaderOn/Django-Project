from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.comments import CommentSerializer
from comments_app.models import Comments


class CommentsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()
    filter_backends = [filters.OrderingFilter]