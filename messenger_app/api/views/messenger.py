from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.messenger import MessengerSerializer
from ...models import Messenger


class MessengerViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    """Создаём класс вьюсет чата"""
    serializer_class = MessengerSerializer
    queryset = Messenger.objects.all()