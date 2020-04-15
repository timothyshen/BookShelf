from rest_framework import serializers
from books.serializers import BookSerializer
from .models import *


class ReaderSerializer(serializers.ModelSerializer):
    role = serializers.CharField(default='Reader')

    class Meta:
        model = Reader
        fields = ('role', 'is_user_vip', 'vip_validate')
        depth = 1


class AuthorSerializer(serializers.ModelSerializer):
    role = serializers.CharField(default='Author')
    book_id = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ('role', 'contract_number', 'book_id')
        depth = 1


class UserProfileSerializer(serializers.ModelSerializer):
    # role_display = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        # fields = ('gender', 'birthday', 'icon', 'role', 'role_display')
        fields = ('gender', 'birthday', 'icon', 'role')
        depth = 1

    # def get_role_display(self, obj):
    #     if obj.role == 'Author':
    #         serializers_choice = AuthorSerializer(obj.author)
    #         return serializers_choice.data
    #     elif obj.role == 'Reader':
    #         serializers_choice = ReaderSerializer(obj.reader)
    #         return serializers_choice.data


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    # profile_data = serializers.SerializerMethodField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'profile',)

        depth = 1

    # def get_profile_data(self, obj):
    #     return UserProfileSerializer(obj.profile).data

    def create(self, validated_data):
        profile = validated_data.pop('profile', None)
        user = User.objects.create(**validated_data)
        if profile is not None:
            profile_data = profile.pop('profile', None)
            new_profile = Profile.objects.create(user=user, **profile)
            if profile_data is not None:
                if profile_data.get('role',profile.role) == 'reader':
                    Reader.objects.create(user=new_profile, **profile_data)
                elif profile_data.get('role',profile.role) == 'author':
                    Author.objects.create(user=new_profile, **profile_data)
        return user

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
