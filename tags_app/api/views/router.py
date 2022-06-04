from rest_framework import routers
from .tags import TagViewSet


api_router = routers.DefaultRouter()
api_router.register('tags', TagViewSet)