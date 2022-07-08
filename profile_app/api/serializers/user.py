from django.contrib.auth.models import User
from profile_app.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер профиля"""
    class Meta:
        model = Profile
        fields = ['avatar', 'phone', 'about', 'github_link']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Создаем класс сериалайзер User"""
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'profile')