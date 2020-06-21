from abc import ABC

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from books.serializers import BookSerializer, ChapterSerializer
from .models import Bookcase, BookMark


class BookCaseDetailSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Bookcase
        fields = ('user', 'book', 'id')


class BookMarkSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()

    class Meta:
        model = BookMark
        fields = '__all__'


class BookCaseSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault()
    # )
    user = serializers.CurrentUserDefault()

    class Meta:
        model = Bookcase
        validators = [
            UniqueTogetherValidator(
                queryset=Bookcase.objects.all(),
                fields=('user', 'book'),
                message='Already existing in the bookcase'
            )
            # ,
            # UniqueTogetherValidator(
            #     queryset=Bookcase.objects.all(),
            #     fields=('book', 'bookmark'),
            #     message='Already existing bookmark for the book'
            # )
        ]

        fields = ('id','user', 'book', 'bookmark')
