from rest_framework import serializers
from likes_app.models import LikePost, LikeComment


class LikePostSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер лайков постов"""
    class Meta:
        model = LikePost
        fields = '__all__'                                 # вывод всех полей
        read_only_fields = ['user',]


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )


class LikeCommentSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер лайков комментариев"""
    class Meta:
        model = LikeComment
        fields = '__all__'
        read_only_fields = ['user',]


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )