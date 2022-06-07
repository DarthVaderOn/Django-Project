from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.comments import CommentSerializer
from comments_app.models import Comments


class CommentsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()