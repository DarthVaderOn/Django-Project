from rest_framework import serializers
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
    # media_uploaded_at = serializers.DateTimeField(source='file.uploaded_at', allow_null=True, read_only=True)
    tag = TagSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    likes_comment_count = serializers.SerializerMethodField()


    def get_likes_count(self, instance) -> int:
        return instance.likes.count()


    def get_comments_count(self, instance) -> int:
        return instance.comments.count()


    def get_likes_comment_count(self, instance) -> int:
        return instance.likes_comment.count()