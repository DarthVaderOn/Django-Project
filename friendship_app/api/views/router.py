from rest_framework import routers
from .friendship import FriendshipViewSet, FollowViewSet


api_router = routers.DefaultRouter()
api_router.register('friendship', FriendshipViewSet)
api_router.register('follow', FollowViewSet)