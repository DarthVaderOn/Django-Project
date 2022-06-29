from profile_app.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер профиля"""
    class Meta:
        model = Profile
        fields = '__all__'