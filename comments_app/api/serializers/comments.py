from rest_framework import serializers
from comments_app.models import Comments


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'                                # вывод всех полей
        read_only_fields = ['user']


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )