from rest_framework import serializers
from media_app.api.serializers.media import MediaFileSerializer
from messenger_app.models import Messenger


class MessengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messenger
        exclude = ['id']
        read_only_fields = ('id', 'user', 'created_at',)
        extra_kwargs = {
            'file': {
                'required': True,
                'write_only': True,
                'help_text': 'ID медиа файла',
            },
        }


    media = MediaFileSerializer(source='file', allow_null=False, read_only=True)