from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import *

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'password', 'email', 'is_active')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ReaderSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = Reader
        fields = '__all__'
