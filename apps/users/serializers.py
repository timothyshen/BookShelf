from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ('user', 'gender')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        profile = Profile.objects.create(**validated_data)
        User.objects.create(user=profile, **user_data)
        return profile

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        instance.gender = validated_data.get('gender', instance.gender)
        user = instance.user
        instance.save()
        user.username = user_data.get('username', user.username)
        user.password = user_data.get('password', user.password)
        user.email = user_data.get('email', user.password)
        user.save()
        return instance


class ReaderSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop('user')

    class Meta:
        model = Reader
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = Author
        fields = '__all__'
