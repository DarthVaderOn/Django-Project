from rest_framework import serializers
from likes_app.models import LikePost, LikeComment


class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePost
        fields = '__all__'                          # вывод всех полей
        # exclude = ('is_public',)                  # исключения
        # fields и exclude - должно быть одно из них, два вместе НЕ ДОПУСКАЕТСЯ !
        read_only_fields = ('user',)


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )


class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComment
        fields = '__all__'                          # вывод всех полей
        # exclude = ('is_public',)                  # исключения
        # fields и exclude - должно быть одно из них, два вместе НЕ ДОПУСКАЕТСЯ !
        read_only_fields = ('user',)


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )