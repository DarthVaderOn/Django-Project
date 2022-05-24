from rest_framework import serializers
from ...models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'                          # вывод всех полей
        # exclude = ('is_public',)                  # исключения
# fields и exclude - должно быть одно из них, два вместе НЕ ДОПУСКАЕТСЯ !
        read_only_fields = ('id', 'user', 'is_public')

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )