from rest_framework import serializers
from likes_app.models import LikePost, LikeComment
from profile_app.api.serializers.user import UserSerializer


class LikePostSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер лайков постов"""
    user = UserSerializer(read_only=True)


    class Meta:
        model = LikePost
        fields = ['id', 'post', 'user', 'publisher_user']       # вывод всех полей
        read_only_fields = ['user',]


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )


class LikeCommentSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер лайков комментариев"""
    user = UserSerializer(read_only=True)


    class Meta:
        model = LikeComment
        fields = ['id', 'comment', 'user', 'publisher_user']
        read_only_fields = ['user',]


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )