from rest_framework import serializers
from media_app.api.serializers.media import MediaFileSerializer
from profile_app.api.serializers.user import UserSerializer
from publication_app.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер постов"""
    class Meta:
        model = Post
        exclude = ['is_public']
        read_only_fields = ('id', 'user', 'is_public')
        extra_kwargs = {
            'file': {
                    'required': True,
                    'write_only': True,
                    'help_text': 'ID медиа файла',
                },
            }


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )


    # media = serializers.URLField(source='file.file.url', read_only=True)
    # media_uploaded_at = serializers.DateTimeField(source='file.uploaded_at', allow_null=True, read_only=True)
    media = MediaFileSerializer(source='file', allow_null=False, read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)


    def get_likes_count(self, instance) -> int:
        """Отображаем общее количество лайков постов"""
        return instance.likes.count()


    def get_comments_count(self, instance) -> int:
        """Отображаем общее количество комментариев к посту"""
        return instance.comments.count()