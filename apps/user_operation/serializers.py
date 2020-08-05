# _*_ coding: utf-8 _*_
from rest_framework import serializers
from .models import *
from users.models import Profile, User
from books.serializers import Book
__author__ = 'Tim'
__date__ = '03/08/2020 21:26'


class UserProfile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('icon',)


class UserInfo(serializers.ModelSerializer):
    profile = UserProfile(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'profile')

class BookInfo(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'book_name')


class UserMessageTwo(serializers.ModelSerializer):
    class Meta:
        model = UserComment
        fields = "__all__"


class UserMessage(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    book = BookInfo()

    class Meta:
        model = UserComment
        fields = "__all__"

class UserMessageForAuthor(serializers.ModelSerializer):
    user = UserInfo(read_only=True)
    book = BookInfo()

    class Meta:
        model = UserComment
        fields = "__all__"

class UserMessageList(serializers.ModelSerializer):
    user = UserInfo(read_only=True)

    class Meta:
        model = UserComment
        fields = "__all__"
