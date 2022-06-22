from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.likes import LikePostSerializer, LikeCommentSerializer
from likes_app.models import LikePost, LikeComment


class LikePostsViewSet(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    serializer_class = LikePostSerializer
    queryset = LikePost.objects.all()


class LikeCommentsViewSet(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.all()