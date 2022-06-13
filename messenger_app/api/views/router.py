from rest_framework import routers
from .messenger import MessengerViewSet


api_router = routers.DefaultRouter()
api_router.register('messenger', MessengerViewSet)