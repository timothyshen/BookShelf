from abc import ABC

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from books.serializers import BookSerializer
from .models import Bookcase


class BookDetailSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Bookcase
        fields = ('user', 'book', 'id')


class BookcaseSerializer(serializers.ModelSerializer):
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
        ]

        fields = ('user', 'book', 'id')
