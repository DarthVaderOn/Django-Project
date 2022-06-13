from rest_framework import routers
from .likes import LikePostsViewSet, LikeCommentsViewSet


api_router = routers.DefaultRouter()
api_router.register('likes', LikePostsViewSet)
api_router.register('likes_comment', LikeCommentsViewSet)