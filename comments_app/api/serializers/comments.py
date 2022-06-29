from rest_framework import serializers
from comments_app.models import Comments


class CommentSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер комментариев"""
    class Meta:
        model = Comments
        fields = '__all__'                                # вывод всех полей
        read_only_fields = ['user']


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )


    likes_comment_count = serializers.SerializerMethodField()


    def get_likes_comment_count(self, instance) -> int:
        return instance.likes_comment.count()