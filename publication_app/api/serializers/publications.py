from rest_framework import serializers
from comments_app.api.serializers.comments import CommentSerializer
from likes_app.api.serializers.likes import LikePostSerializer
from media_app.api.serializers.media import MediaFileSerializer
from publication_app.models import Post
from tags_app.api.serializers.tags import TagSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['is_public']
        read_only_fields = ('id', 'user', 'is_public',)
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
    media = MediaFileSerializer(source='file', allow_null=False, read_only=True)
    tag = TagSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikePostSerializer(many=True, read_only=True)