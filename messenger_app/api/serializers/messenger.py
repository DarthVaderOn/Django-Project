from rest_framework import serializers
from media_app.api.serializers.media import MediaFileSerializer
from messenger_app.models import Messenger


class MessengerSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер мессенджера"""
    class Meta:
        model = Messenger
        fields = '__all__'
        read_only_fields = ('id', 'sender', 'created_at',)
        extra_kwargs = {
            'file': {
                'required': False,
                'write_only': True,
                'help_text': 'ID медиа файла',
            },
        }

    publisher_sender = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='sender',
    )

    media = MediaFileSerializer(source='file', allow_null=False, read_only=True)