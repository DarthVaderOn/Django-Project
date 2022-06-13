from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.friendship import FriendshipSerializer, FollowSerializer
from ...models import FriendshipRequest, FollowRequest


class FriendshipViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    serializer_class = FriendshipSerializer
    queryset = FriendshipRequest.objects.all()


class FollowViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    serializer_class = FollowSerializer
    queryset = FollowRequest.objects.all()