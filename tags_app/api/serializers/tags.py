from rest_framework import serializers
from tags_app.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'                          # вывод всех полей
        # exclude                                   # исключения
        # fields и exclude - должно быть одно из них, два вместе НЕ ДОПУСКАЕТСЯ !