from rest_framework import filters, permissions
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.comments import CommentSerializer
from comments_app.models import Comments


class CommentsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    """Создаём класс вьюсет комментариев"""
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_time']
    permission_classes = [permissions.IsAuthenticated]                       # просмотр комментариев только для авторизованного пользователя