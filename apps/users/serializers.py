from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile

        # fields = ('gender', 'birthday', 'icon', 'role', )
        exclude = ['user']
        depth = 1


class UserDetailSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'profile',)
        depth = 1

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        profile.gender = profile_data.get('gender', profile.gender)
        profile.birthday = profile_data.get('birthday', profile.birthday)
        profile.icon = profile_data.get('icon', profile.icon)
        profile.role = profile_data.get('role', profile.role)
        profile.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'profile',)

        depth = 1

    def create(self, validated_data):
        profile = validated_data.pop('profile', None)
        user = User.objects.create(**validated_data)
        if profile is not None:
            Profile.objects.create(user=user, **profile)
        return user
