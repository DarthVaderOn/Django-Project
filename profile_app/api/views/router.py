from rest_framework import routers
from .user import UserView


api_router = routers.DefaultRouter()
api_router.register('profile', UserView)