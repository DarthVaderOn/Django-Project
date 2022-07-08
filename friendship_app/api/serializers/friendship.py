from rest_framework import serializers
from friendship_app.models import FriendshipRequest, FollowRequest


class FriendshipSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер дружбы"""
    class Meta:
        model = FriendshipRequest
        fields = '__all__'                                # вывод всех полей
        read_only_fields = ['user', 'friendship_result',]


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )


class FollowSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер подписки"""
    class Meta:
        model = FollowRequest
        fields = '__all__'                                # вывод всех полей
        read_only_fields = ['user']


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )