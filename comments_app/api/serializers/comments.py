from rest_framework import serializers
from comments_app.models import Comments
from profile_app.api.serializers.user import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер комментариев"""
    user = UserSerializer(read_only=True)


    class Meta:
        model = Comments
        fields = ['id', 'text', 'created_at', 'post', 'likes_comment_count', 'user', 'publisher_user']
        read_only_fields = ['user']


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )


    likes_comment_count = serializers.SerializerMethodField()


    def get_likes_comment_count(self, instance) -> int:
        return instance.likes_comment.count()