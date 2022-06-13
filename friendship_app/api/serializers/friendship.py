from rest_framework import serializers
from friendship_app.models import FriendshipRequest, FollowRequest


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = '__all__'                                # вывод всех полей
        read_only_fields = ['user']


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowRequest
        fields = '__all__'                                # вывод всех полей
        read_only_fields = ['user']


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )